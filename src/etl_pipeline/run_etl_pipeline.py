from .etl_pipeline import EtlPipeline

from ..utils import PDFExtractor
from ..utils import OpenAi_Embedder
from ..utils import MyWeaviate

def run_etl_pipeline():
    directory_path = 'locsid4sme1\data'
    etl = EtlPipeline(PDFExtractor(directory_path),OpenAi_Embedder(),MyWeaviate())
    etl.run(directory_path)
    
    pass

if __name__ == '__main__': 
    run_etl_pipeline()