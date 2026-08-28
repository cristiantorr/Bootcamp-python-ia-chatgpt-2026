import requests


url = "http://localhost:11434/api/generate"

MODEL = "llama3.2"


payload = {
    "model": MODEL,
    "prompt": "Explícame qué es Python en una frase.",
    "stream": False
}

response = requests.post(url, json=payload) # Aquí enviamos el payload
print(response.json()["response"])