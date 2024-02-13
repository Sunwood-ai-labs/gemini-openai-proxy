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



# 画像をBase64形式にエンコードする関数
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# 画像のパス
image_path = "data/warabi.jpg"

# 画像をBase64でエンコード
base64_image = encode_image(image_path)

# APIリクエストの設定
url = "http://localhost:8080/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {YOUR_GOOGLE_AI_STUDIO_API_KEY}"
}
data = {
    "model": "gpt-4-vision-preview",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": "What’s in this image?"},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }],
    "temperature": 0.7
}

# APIリクエストを送信し、応答を表示
response = requests.post(url, json=data, headers=headers)
print(response.text)

# {"id":"chatcmpl-7f17b8f5dc8f4d36aee9dad8935b0d25","object":"chat.completion","created":1707785494,"model":"gemini-pro","choices":[{"index":0,"message":{"role":"assistant","content":" The image contains a plate of mochi, a Japanese rice cake, dusted with kinako, a roasted soybean flour."},"finish_reason":"stop"}],"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0},"system_fingerprint":""}