import whisper
import ollama
import sounddevice as sd
from ollama import chat, ChatResponse, generate
import process
import record #record.py
import search

# Config
ENABLE_WEB_SEARCH = True

def main(result_text): #process text
    if ENABLE_WEB_SEARCH and search.is_search_query(result_text):
        print("\n[Searching the web...]\n")
        search_results = search.search_web(result_text)
        print(search_results)
        
        context_prompt = f"""Based on this search result, answer the user's question.

User question: {result_text}

Search results:{search_results}

Provide a helpful answer:"""
        
        response = generate(
            model='tinyllama:latest',
            prompt=context_prompt,
            stream=True,
        )
        print("\n[Answer]")
        for chunk in response:
            print(chunk['response'], end='', flush=True)
    else:
        stream = chat(
            model='tinyllama:latest',
            messages=[{'role': 'user', 'content': result_text}],
            stream=True,
        )

        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True) 


if __name__ == "__main__":
    pass

