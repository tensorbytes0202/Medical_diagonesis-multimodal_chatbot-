import requests

HF_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HF_TOKEN = "YOUR_HF_TOKEN"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def chatbot_response(user_input: str):
    payload = {"inputs": user_input}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    result = response.json()
    return result[0]["generated_text"]