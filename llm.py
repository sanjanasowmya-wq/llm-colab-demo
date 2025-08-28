import os
import json
from tavily import TavilyClient

os.environ["TAVILY_API_KEY"] = "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"

def search_and_print(query):
    api_key = os.environ["TAVILY_API_KEY"]
    tavily_client = TavilyClient(api_key=api_key)

    response = tavily_client.search(query)

    # Print results to console
    for result in response["results"]:
        print(f"Title: {result['title']}")
        print(f"Content: {result['content']}")
        print(f"URL: {result['url']}")
        print("-" * 50)

    # Save results to JSON file
    with open("results.json", "w") as f:
        json.dump(response, f, indent=4)

    print("\n✅ Results also saved to results.json")

search_and_print("what is open ai")
