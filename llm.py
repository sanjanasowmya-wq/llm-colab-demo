import os
from tavily import TavilyClient

os.environ["TAVILY_API_KEY"] = "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"

def search_and_print(query):
    api_key = os.environ["TAVILY_API_KEY"]
    tavily_client = TavilyClient(api_key=api_key)

    response = tavily_client.search(query)

    for result in response["results"]:
        print(f"Title: {result['title']}")
        print(f"Content: {result['content']}")
        print(f"URL: {result['url']}")
        print("-" * 50)

search_and_print("what is open ai")
