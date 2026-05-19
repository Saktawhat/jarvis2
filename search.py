import subprocess
import json
from typing import Optional


# TODO: รองรับภาษาไทย


WEB_SEARCH_TRIGGERS = [
    "search for",
    "look up",
    "what is",
    "who is",
    "when did",
    "where is",
    "how to",
    "current",
    "latest",
    "today",
    "weather",
    "news",
]

def is_search_query(text: str) -> bool:
    text_lower = text.lower()
    return any(trigger in text_lower for trigger in WEB_SEARCH_TRIGGERS)

def search_web(query: str, num_results: int = 5) -> str:
    try:
        result = subprocess.run(
            ["websearch", "--query", query, "--num_results", str(num_results)],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout
    except FileNotFoundError:
        return search_web_fallback(query)

def search_web_fallback(query: str, num_results: int = 3) -> str:
    import urllib.parse
    import urllib.request
    
    encoded_query = urllib.parse.quote(query)
    url = f"https://duckduckgo.com/html/?q={encoded_query}&format=json"
    
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            results = []
            for item in data.get("results", [])[:num_results]:
                results.append(f"- {item.get('title', '')}: {item.get('url', '')}")
            return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Search failed: {str(e)}"

def fetch_url(url: str) -> str:
    try:
        result = subprocess.run(
            ["webfetch", "--url", url],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.stdout[:2000]
    except Exception as e:
        return f"Fetch failed: {str(e)}"