from typing import List
from kiosk.kiosk import Kiosk
from kiosk.kiosk import Document
from kiosk.kiosk import DocumentCollection
import pytest
from langchain.embeddings.base import Embeddings


@pytest.fixture
def test_documents() -> DocumentCollection:
    return DocumentCollection()


class MockEmbedder(Embeddings):
    def embed_query(self, text: str) -> List[float]:
        return [1, 1, 1]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [[]]


class TestKiosk:
    def setup_method(self, test_documents):
        """Populates the vectorstore with a few documents"""
        print("ran setup")

        documents = DocumentCollection(
            documents=[
                Document(text="test document", embeddings=[1, 2, 3]),
                Document(text="What is this document about", embeddings=[1, 1, 1]),
            ]
        )
        self.kiosk = Kiosk(documents=documents, embedder=MockEmbedder)

    # @pytest.mark.skip(reason="Not implemented yet")
    def test_similarity_search(self):
        """ """
        # query a text against the existing documents
        test_query = "What is this document about"
        # make sure that the documents are returned in the right order
        documents = self.kiosk.query(test_query)
        assert len(documents) > 0
        search_result = documents[0]
        assert search_result["document"].text == test_query
        assert search_result["score"] == 1.0

    @pytest.mark.skip(reason="Not implemented yet")
    def test_similarity_search_meta_data_filter(self):
        pass

    def teardown_method(self):
        print("ran teardown - doesn't do anything for now")
        pass
