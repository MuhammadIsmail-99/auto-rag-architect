from typing import List, Dict, Any
from architect.strategies import DenseRetrieval, HybridRetrieval

class RAGArchitect:
    def __init__(self, data_source: str):
        self.data_source = data_source
        self.strategy = None

    def analyze_data_structure(self) -> str:
        # Strategic logic to determine the best RAG strategy
        # In a real app, this would analyze file types, density, etc.
        print(f"Analyzing data from: {self.data_source}")
        return "hybrid"

    def instantiate_pipeline(self, strategy_type: str):
        if strategy_type == "hybrid":
            self.strategy = HybridRetrieval()
        else:
            self.strategy = DenseRetrieval()
        
        print(f"Pipeline instantiated with {strategy_type} strategy.")

    def query(self, text: str) -> List[str]:
        if not self.strategy:
            raise ValueError("Pipeline not instantiated.")
        return self.strategy.retrieve(text)
