from datetime import datetime

import pandas as pd
from tavily import TavilyClient


class ResearchDataCollectorAgent:
    def __init__(self, topic, result_count=10):
        self.topic = topic
        self.result_count = result_count
        self.results = []

        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY environment variable is missing.")

        self.client = TavilyClient(api_key="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")

    def search_web(self):
        response = self.client.search(
            query=self.topic,
            search_depth="basic",
            max_results=self.result_count,
            include_answer=True
        )

        for item in response.get("results", []):
            self.results.append({
                "Topic": self.topic,
                "Title": item.get("title"),
                "URL": item.get("url"),
                "Content": item.get("content"),
                "Score": item.get("score"),
                "Collected Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

    def save_to_excel(self):
        if not self.results:
            print("No result found.")
            return

        file_name = self.topic.replace(" ", "_").lower() + "_research_results.xlsx"

        df = pd.DataFrame(self.results)
        df.to_excel(file_name, index=False)

        print(f"Excel file created: {file_name}")

    def run(self):
        print(f"Searching for: {self.topic}")
        self.search_web()
        self.save_to_excel()


if __name__ == "__main__":
    topic = input("Enter research topic: ")

    agent = ResearchDataCollectorAgent(
        topic=topic,
        result_count=10
    )

    agent.run()