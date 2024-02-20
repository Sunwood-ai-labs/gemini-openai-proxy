import base64
import requests
import os
from dotenv import load_dotenv
import pprint
import json

# .envファイルから環境変数を読み込む
load_dotenv()

# .envファイルからAPIキーを読み込む
YOUR_GOOGLE_AI_STUDIO_API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
# or 
# YOUR_GOOGLE_AI_STUDIO_API_KEY = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

url = "http://ThunderLynx:7070/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {YOUR_GOOGLE_AI_STUDIO_API_KEY}"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

response = requests.post(url, json=data, headers=headers)

print(response.text)