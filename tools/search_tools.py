from langchain.tools import tool
import json, requests, os
class SearchTool():
    @tool("Search the internet")
    def search_internet(query):
        """
        Searches the internet for the given query and returns the top 4 results."""
        top_results_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            "X-API-KEY": os.environ['SERPER_API_KEY'], 
            "content-type": 'application/json'
        }
        response = requests.request(
            "POST",
            url,
            headers=headers,
            data=payload
        )

        if 'organic' not in response.json():
            return "Sorry I couldn't find anything about that, there could be a error with your server"
        else:
            results =response.json()['organic']
            string=[]
            for result in results[:top_results_to_return]:
                string.append("; ". join([
                    f"Title: {result['title']}", f"Link: {result['link']}", f"Snippet: {result['snippet']}"
                ]))
            return string