from typing import Dict, List
from kiosk.utils import cosine_similarity
from langchain.embeddings.base import Embeddings
from typing import Type, Optional, TypedDict, Dict


class Document:
    """
    A data structure consisting of text accompanied with it's corresponding text embeddings
    """

    def __init__(self, text: str, embeddings: List[float]):
        self.text = text
        self.embeddings = embeddings


class SearchResult(TypedDict):
    score: float
    document: Document


class DocumentCollection:
    """
    A collection of documents that implements CRUD operations over a document

    in addition, querying similar documents to a piece of text based on similarity search
    """

    def __init__(self, documents: Optional[List[Document]] = None):
        print(f"document collection documents: {documents}")
        if documents:
            self.documents = documents
        else:
            self.documents: List[Document] = []

    def add_document(self, document: Document):
        self.documents.append(document)

    def similarity_search(
        self, query_embeddings: List[float], k: int
    ) -> List[SearchResult]:
        results = []
        print(f"len documents: {len(self.documents)}")
        for doc in self.documents:
            similarity_score = cosine_similarity(doc.embeddings, query_embeddings)
            results.append({"score": similarity_score, "document": doc})

        sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

        if k > len(sorted_results):
            k = len(sorted_results)
        top_k_results = sorted_results[:k]

        return top_k_results

    def similarity_search_filter_by_meta_data(self):
        raise Exception("Not implemented")
        pass


class Kiosk:
    """
    A Simple implementation of a vector store
    """

    def __init__(self, documents: DocumentCollection, embedder: Type[Embeddings]):
        print(f"documents: {documents.documents}")
        if not documents:
            self.documents = DocumentCollection()
        else:
            self.documents = documents

        self.embedder = embedder()

    def add_document(self, document: Document):
        try:
            self.documents.add_document(document)
        except Exception as e:
            raise e

    def query(self, query: str, k: int = 4):
        """Given a query string, find the most similar documents to it inside the document store

        Args:
            query (str): TODO: write docstring
            k: (int): get k most similar documents to the query paramter
        """

        query_embedding: List[float] = self.embedder.embed_query(text=query)
        return self.documents.similarity_search(
            query_embedding, k=k
        )  # I assume that I always use the same embedding function, for simplicity
