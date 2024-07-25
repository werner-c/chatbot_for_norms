from .completion import Completion
from openai import OpenAI
import os


class OpenAi_Completion(Completion):
    def __init__(self):
        self.name = 'OpenAiCompletion'

    def make_completion(self, text_input: str, verbose = False) -> str:
        '''
        This method takes an text as input and hands it over to a LLM. The genrated answer is returned.

        Args:
            - text (str): The input text or prompt for the LLM
            - verbose (bool): Toggles print output for detailed answer object from LLM. Defaults to False.

        Returns:
            - str: The answer from the LLM
        '''
        
        client = OpenAI(
            api_key=os.environ['OPENAI_KEY']
        )

        messages = [
            {"role": "user", "content": text_input}
        ]

        completion = client.chat.completions.create(
            model=os.environ['COMPLETION_MODEL'],  
            messages=messages,
            seed=4242
        )
        return completion.choices[0].message.content

#comp = OpenAi_Completion()
#print(comp.make_completion("How are you"))