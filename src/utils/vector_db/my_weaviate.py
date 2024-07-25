from .vector_db import VectorDB
import os
import weaviate
from weaviate.classes.config import Property, DataType
from weaviate.classes.query import Filter


class MyWeaviate(VectorDB):
    def __init__(self, name = eval(os.environ['WEAVIATE_CLASS'])['name']):
        self.name = name
    
    def is_live(self) -> bool:
        '''
        This method returns if the MyWeaviate is live.
        
        Returns:
            bool: True if it is live, else False.
        '''
        try:
            client = self.get_client()        
            client.close()
            return True
        except Exception as e:
            return False
    
    def add_elements(self, elements: list):
        '''
        This method adds the elements to the vector database.
        
        Args:
            elements (list): The elements to add.
        '''
        client = self.get_client()
        try:
            collection = client.collections.get(self.name)
            with collection.batch.dynamic() as batch:
                for e in elements:
                    if len(self.get_elements(e['properties'], limit = None)) == 0:
                        batch.add_object(
                            properties = e['properties']
                            #vector = e['vector']
                        )
        
        finally:
            client.close()    
    
    def create_collection(self):
        '''
        This method creates a collection specified by self.name and the properties from WEAVIATE_CLASS
        '''
        prop_dict = eval(os.environ['WEAVIATE_CLASS'])['properties']            
        properties = [Property(name=k, data_type=prop_dict[k]) for k in prop_dict.keys()]
        
        client = self.get_client()
        try:
            if self.name not in self.get_all_collections():
                client.collections.create(
                    self.name,
                    properties=properties
                )
            else:
                print("This class already exists")
        finally:
            client.close()
           
    def delete_collections(self, collections: list[str]):
        client = self.get_client()
        try:
            for collection in collections:                
                client.collections.delete(collection)
        finally:
            client.close()
       
    def delete_elements_by_id(self, ids: list[str]):
        '''
        This method delets elements from the vektor databse by the id.
        Recomended Usage: Use get_elements() to extract the ids from the returned list of dicts. USe those ids for deletion.
        '''
        client = self.get_client()
        try:
            collection = client.collections.get(self.name)
            for id in  ids:
                collection.data.delete_by_id(id)
        finally:
            client.close()
     
    def get_all_collections(self) -> list[str]:
        '''
        This method returns the names of all existing collections.
        
        Returns:
            list[str]: The list of names.
        '''
        client = self.get_client()
        try:
            return client.collections.list_all().keys()
        finally:
            client.close()
         
    def get_client(self):
        '''
        This method creates a client, to connect to the weaviate docker. The connection needs to be terminated manually.
        
        Return:
            weaviate.Client: The client to connect to the weaviate docker.
        '''
        client = weaviate.connect_to_custom(
            http_host=os.environ['WEAVIATE_HTTP_HOST'],
            http_port=os.environ['WEAVIATE_HTTP_PORT'],
            http_secure=False,
            grpc_host=os.environ['WEAVIATE_GRPC_HOST'],
            grpc_port=os.environ['WEAVIATE_GRPC_PORT'],
            grpc_secure=False,
            #headers={
            #    "X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")  # Or any other inference API keys
            #}
        )
        return client
    
    def get_elements(self, filters: dict, limit = int, verbose = False) -> list[dict]:
        '''
        This querrys the database and returns all elements taht fits the requirements.
        
        Args:
            filters (dict): The filters that will be applied e.g. {'path': 'value.pdf', ...}
            limit (int): The limit of elements you want to receive. Use 'None' for all elements.
            verbose (bool): Toggle the print. Defaults to False.
        
        Returns:
            list[dict]: The list of searched elements. Each element is represented by an dict with the keys 'id' and 'properties'.
        '''
        client = self.get_client()
        try:
            collection = client.collections.get(self.name)
            if len(filters) == 0:                 
                all_elements = collection.iterator()
                results = []               
                for item in all_elements:
                    results.append({'id': item.uuid, 'properties': item.properties})
                    if verbose:
                        print(item.uuid, item.properties)
                if limit != None:
                    return results[:limit]
                return results
                
            else:
                weaviate_filters = [Filter.by_property(k).equal(filters[k]) for k in filters.keys()]
                combined_filters = weaviate_filters[0]
                for i in range(1, len(filters)):
                    combined_filters = combined_filters & weaviate_filters[i]
                querry_results = collection.query.fetch_objects(
                    filters=combined_filters,
                    limit=limit
                )
                response = []
                for o in querry_results.objects:
                    response.append({'id': o.uuid, 'properties': o.properties})
                return response
        finally:
            client.close()
     
    def search(self, query: str, question_embedding: list[float], filters: dict, limit: int) -> list:
        client = self.get_client()
        try:
            querry_results = ''
            collection = client.collections.get(self.name)
            if len(filters) > 0:
                weaviate_filters = [Filter.by_property(k).equal(filters[k]) for k in filters.keys()]
                combined_filters = weaviate_filters[0]
                for i in range(1, len(filters)):
                    combined_filters = combined_filters & weaviate_filters[i]                
                querry_results = collection.query.hybrid(
                    query = query,
                    vector=question_embedding,
                    filters=combined_filters, 
                    limit = limit
                )
            else:
                querry_results = collection.query.hybrid(
                    query=query,
                    vector=question_embedding,
                    limit = limit
                )
            response = []
            for o in querry_results.objects:
                response.append({'id': o.uuid, 'properties': o.properties})
            return response            
        finally:
            client.close()