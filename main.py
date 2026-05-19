import whisper
import ollama
import sounddevice as sd
from ollama import chat, ChatResponse, generate
import record #record.py
import search

# Config
model = whisper.load_model("small")
ENABLE_WEB_SEARCH = True

def DecodeAudio(audio_file): # แปล Speak to text
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio_file) # หามาใส่เด้อหล่า
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    return(result.text)

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
    audio_file = record.record_audio() #filename.function_name
    result = DecodeAudio(audio_file)
    main(result)


