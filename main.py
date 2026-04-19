import argparse
from architect.rag_engine import RAGArchitect

def main():
    parser = argparse.ArgumentParser(description="Auto-RAG Architect CLI")
    parser.add_argument("--data", required=True, help="Path to data source")
    parser.add_argument("--query", help="Test query for the architected pipeline")
    
    args = parser.parse_args()
    
    # 1. Initialize Architect
    architect = RAGArchitect(args.data)
    
    # 2. Analyze and Instantiate
    strategy = architect.analyze_data_structure()
    architect.instantiate_pipeline(strategy)
    
    # 3. Test Query
    if args.query:
        results = architect.query(args.query)
        print(f"\nResults: {results}")

if __name__ == "__main__":
    main()
