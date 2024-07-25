from ..wrapper import Document, Chunk
from typing import List
import tiktoken

def chunk(document: Document, chunk_size = 100, overlap = 20) -> List[Chunk]:
    """
    Splits a document into chunks of specified size with a specified overlap.

    Args:
        document (Document): The document to be chunked.
        chunk_size (int, optional): The size of each chunk. Defaults to 100.
        overlap (int, optional): The overlap between consecutive chunks. Defaults to 20.

    Returns:
        List[Chunk]: A list of Chunk objects representing the chunks of the document.
    """
    
    enc = tiktoken.encoding_for_model('gpt-3.5-turbo')
    chunks = []
    coverage = 0
    number = 0
    tokenized = enc.encode(document.text)
    token_count = len(tokenized)
    while coverage < token_count:
        tmp_coverage = (coverage + chunk_size) - overlap
        # edge case: last chunk
        if tmp_coverage + overlap > token_count:
            tmp_coverage = token_count
        chunk_text = tokenized[coverage:tmp_coverage + overlap]
        chunks.append(Chunk(document.filename, enc.decode(chunk_text), number))
        coverage = tmp_coverage
        number += 1
    return chunks