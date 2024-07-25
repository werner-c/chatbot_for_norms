import os
 
class Document:
    '''
    This class represents a document.
    '''
    def __init__(self, filename: str, text: str):
        '''
        This method creates a new Document.
        
        Args:
            filename (str): The filename (or path) of the Document. This value is unique.
            text (str): the text of the entoire document.
        '''
        self.filename = filename
        self.text = text
        
    def to_dict(self):
        '''
        This method returns the Document as a dictionary.
        
        Returns:
            dict: The dict representation of the Document.
        '''
        return {
            'filename': self.filename,
            'text' : self.text
        }
        
class Chunk:
    '''
    This class represents a single chunk.
    '''
    def __init__(self, filename: str, text: str, number: str):
        '''
        This method creates a new Chunk.
        
        Args:
            filename (str): The filename (or path) of the Document the Chunk is a part of..
            text (str): The text fragment of the entire document that is represented by this chunk.
            number (str): The position of the Chunk. It can be used to bring the chunks in the right order. 
        '''
        self.filename = filename
        self.text = text
        self.number = number
        
    def to_dict(self):
        '''
        This method returns the Document as a dictionary.
        
        Returns:
            dict: The dict representation of the Document.
        '''
        return {
            'path': self.filename,
            'text' : self.text,
            'number': self.number
        }