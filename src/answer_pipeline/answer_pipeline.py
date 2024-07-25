from ..utils import Completion, Embedder, VectorDB


class AnswerGeneration:
    def __init__(
        self, vector_db: VectorDB, embedder: Embedder, completion: Completion
    ) -> None:
        self.vector_db = vector_db
        self.embedder = embedder
        self.completion = completion

    def run(self, question):
        self.vector_db.is_live()
        
        question_embedding = self.embedder.make_embedding(question)
        context = [
            str(c["properties"]) for c in self.vector_db.search(question, question_embedding, {}, limit=3)
        ]
        print("\n\n----------------------------------------------------------\n")
        for c in context:
            print(c + "\n\n----------------------------------------------------------\n")
        prompt = f"Answer the question based on the given context! Only use relevant context thats related to the question. else state that there is no answer included in the context!\n\n question = {question}\n context = {context}\n\nCite the contexts you used for answering the question by their indices in the list of contexts."
        return self.completion.make_completion(prompt)
