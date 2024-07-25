from .answer_pipeline import AnswerGeneration
from ..utils import MyWeaviate, OpenAi_Completion, OpenAi_Embedder

def run_answer_pipeline(question: str):
    ag = AnswerGeneration(
        vector_db=MyWeaviate(),
        embedder=OpenAi_Embedder(),
        completion=OpenAi_Completion()
    )
    
    return ag.run(question)