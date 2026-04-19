from abc import ABC, abstractmethod
from typing import List

class RetrievalStrategy(ABC):
    @abstractmethod
    def retrieve(self, query: str) -> List[str]:
        pass

class DenseRetrieval(RetrievalStrategy):
    def retrieve(self, query: str) -> List[str]:
        return [f"Vector-based result for: {query}"]

class HybridRetrieval(RetrievalStrategy):
    def retrieve(self, query: str) -> List[str]:
        return [f"Semantic + Keyword filtered result for: {query}"]
