from tqdm import tqdm

from ..utils import PDFExtractor
from ..utils import Document
from ..utils import chunk
from ..utils import Embedder
from ..utils import VectorDB

class EtlPipeline:
    '''
    This class represents a EtlPipeline
    '''

    def __init__(self, loader: PDFExtractor, embedder: Embedder, vector_db: VectorDB):
        self.loader = loader
        self.embedder = embedder
        self.vector_db = vector_db
        self.vector_db.is_live()
        
    def run(self, files_location) -> None:
        self.vector_db.create_collection()
        loader = PDFExtractor(directory_path=files_location)
        files = loader.pdf_paths
        if self.vector_db.is_live():
            
            #! changed into loop!
            for file in files:
                print(f"first len: {len(self.vector_db.get_elements({}, None))}")
                document = Document(file, loader.extract_text_from_pdf(file))
                chunks = chunk(document,chunk_size=500, overlap=50)
                vectors = []
                for c in tqdm(chunks):
                    vector = self.embedder.make_embedding(c.text)
                    vectors.append(vector)
                elements = []
                for i, vector in tqdm(enumerate(vectors)):
                    element = {
                        'properties': chunks[i].to_dict(),
                        'vector': vector
                    }
                    elements.append(element)
                self.vector_db.add_elements(elements)
                print(f"second len: {len(self.vector_db.get_elements({}, None))}")
        else:
            print('ERROR: VectorDB is not live !!!')
        
