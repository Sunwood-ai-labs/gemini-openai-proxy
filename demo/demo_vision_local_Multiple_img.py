import base64
import requests
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# .envファイルからAPIキーを読み込む
YOUR_GOOGLE_AI_STUDIO_API_KEY = os.getenv("GOOGLE_AI_STUDIO_API_KEY")
# or 
# YOUR_GOOGLE_AI_STUDIO_API_KEY = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# dataフォルダ内の.jpgファイルのリストを取得
image_paths = [f"data/{filename}" for filename in os.listdir("data") if filename.endswith(".jpg")]

url = "http://localhost:8080/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {YOUR_GOOGLE_AI_STUDIO_API_KEY}"
}

# 画像データを含むcontentリストの準備
content = [{"type": "text", "text": "What’s in this image?"}]
for image_path in image_paths:
    base64_image = encode_image(image_path)
    content.append({
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
    })

# リクエストデータの準備
data = {
    "model": "gpt-4-vision-preview",
    "messages": [{"role": "user", "content": content}],
    "temperature": 0.7
}

# APIリクエストを送信し、応答を表示
response = requests.post(url, json=data, headers=headers)
print(response.text)

"""
(gemini-openai-proxy) E:\Prj\gemini-openai-proxy>python demo\demo_vision_local_Multiple_img.py
{"id":"chatcmpl-bcb4a636540040c88375b3bb75cf9ff8","object":"chat.completion","created":1707786129,"model":"gemini-pro","choices":[{"index":0,"message":{"role":"assistant","content":" The first image is of a surreal landscape with floating rocks, waterfalls, and a starry sky. The second image is of a steampunk owl with half of its face made of machinery. The third image is of a plate of mochi, a Japanese dessert made of pounded sticky rice."},"finish_reason":"stop"}],"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0},"system_fingerprint":""}
"""

# https://platform.openai.com/docs/guides/vision