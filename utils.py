import requests
import os

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "x-ai/grok-4.1-fast:free"


def call_openrouter(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_API_URL, json=data, headers=headers)

    if response.status_code != 200:
        return f"❌ API Error: {response.text}"

    try:
        return response.json()["choices"][0]["message"]["content"]
    except:
        return "❌ Unexpected API response format."
