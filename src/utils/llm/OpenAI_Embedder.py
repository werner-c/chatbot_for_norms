from .embedder import Embedder
from openai import OpenAI
import os

class OpenAi_Embedder(Embedder):
    def __init__(self):
        self.name = 'OpenAiEmbedder'
        
    def make_embedding(self, text_input: str) -> list[float]:
        '''
        This method takes an text input and calculates the embedding for it.

        Args:
            - text_input (str): The text that should be embedded.

        Returns:
            list[float]: The vector aka the embedding for the input text.
        '''
        client = OpenAI(
            api_key=os.environ['OPENAI_KEY'],
        )   
        response = client.embeddings.create(input=text_input,model=os.environ['EMBEDDING_MODEL'])
        return response.data[0].embedding

#emb = OpenAi_Embedder()
#print(emb.make_embedding("EEEE"))