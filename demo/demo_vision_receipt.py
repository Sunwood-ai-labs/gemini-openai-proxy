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



# 画像をBase64形式にエンコードする関数
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# 画像のパス
image_path = "data/IMG_5322_v2.jpg"

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
            {"type": "text", "text": """
画像のレシートを下記のjsonフォーマットでください

## Output Format (in JSON):
{
  "store": {
    "name": ""
  },
  "transaction": {
    "date": "",
    "time": ""
  },
  "items": [
    {
      "item_name": "",
      "unit_price": ,
      "quantity": ,
      "unit": "",
      "total_price": 
    }
  ],
  "total": {
    "amount": ,
    "points_earned": ,
    "points_used": 
  },
  "payment": {
    "payment_method": ""
  }
}

"""},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
        ]
    }],
    "temperature": 0.7
}

# APIリクエストを送信し、応答を表示
response = requests.post(url, json=data, headers=headers)

# JSONデータをPythonの辞書に変換
data = response.json()  # これが正しい方法です
pprint.pprint(data)
# 'choices'の最初の要素から'message'の'content'を取得して表示
content = data['choices'][0]['message']['content']
print("-------------")
_receipt = content.replace("```json", "").replace("```", "")
print(_receipt)
# JSON文字列をPythonの辞書に変換
receipt = json.loads(_receipt)
# 辞書をJSON形式でファイルに書き込む
# 辞書をJSON形式でファイルに保存
with open('output/receipt_IMG_5322_v2.json', 'w', encoding='utf-8') as f:
    json.dump(receipt, f, ensure_ascii=False, indent=2)