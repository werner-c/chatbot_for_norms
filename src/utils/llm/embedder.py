from dotenv import dotenv_values
from openai import OpenAI


class Embedder:
    def __init__(self):
        self.name = "EmbedderTemplate"

    def make_embedding(self, text_input: str):
        """
        This method takes an text input and calculates the embedding for it.

        Args:
            - text_input (str): The text that should be embedded.

        Returns:
            list[float]: The vector aka the embedding for the input text.
        """
        return []
