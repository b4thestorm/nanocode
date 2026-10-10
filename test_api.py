import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OLLAMA_KEY")

if not api_key:
    print("Error: Ollama_key not found in .env")

url = "https://ollama.com/api/chat"

headers = {
    "Authorization": f"Bearer {api_key}",
    "content-type": "application/json"
}

payload = {
    "model": "gemma4:31b",
    "messages": [{"role": "user", "content": "Hello are you ready to code?"}],
    "stream": False,
}

print("Sending request to Ollama...")
response = requests.post(url, headers=headers, json=payload, timeout=120)

print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("Response:")
    print(json.dumps(response.json(), indent=2))
else:
    print("Error:", response.text)


