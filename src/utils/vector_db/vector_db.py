class VectorDB:
    """
    This class represents a general vector database.
    """

    def __init__(self):
        """
        Initialize a new VectorDB object.
        """
        self.name = "VectorDbTemplate"

    def is_live(self) -> bool:
        """
        This method returns if the VectorDB is live.

        Returns:
            bool: True if it is live, else False.
        """
        return False

    def get_elements(self, filters: dict) -> list:
        """
        Querries the database and returns elements from it.

        Args:
            filters (dict): The filters for the querrie represented with properties as key, and value as value.

        Returns:
            list: All elements from the vector db that fit the filters.
        """
        return []

    def add_elements(self, elements: list):
        """
        Adds new elements to the vector database.

        Args:
            elements (list): The elements to add to the vector database.
        """
        pass

    def delete_elements(self, element_ids: list):
        """
        Deletes elements from the vector databse by the ID.

        Args:
            element_ids (list): The IDs of the elements for deletion.
        """
        pass

    def search(self, question_embedding: list[float], filters=[], limit=3):
        """
        Querries the database and returns the elements that are most similar to the embedding of the question.

        Args:
            question_embedding (list[float]): The embedding of the question.
            filters (dict): The filters for the querrie represented with properties as key, and value as value.
            limit (int): The maximum number of returned elements.

        Returns:
            list: The {limit} elements closest to the question embedding.
        """
        return []
