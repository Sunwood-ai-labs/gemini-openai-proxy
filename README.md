<h1>
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/gemini-openai-proxy/main/docs/geminicat.png" height=300px align="right"/>
Gemini-OpenAI-Proxy
</h1>

Gemini-OpenAI-Proxyは、OpenAI APIプロトコルをGoogle Gemini Proプロトコルに変換するためのプロキシです。これにより、Gemini Proプロトコルを使用するアプリケーションにOpenAIが提供する機能をシームレスに統合することが可能になります。



## デプロイ

### Docker版

Dockerを使用してGemini-OpenAI-Proxyをデプロイすることをお勧めします。簡単なセットアップのために、以下の手順に従ってDockerでデプロイしてください：

```bash
docker run --restart=always -it -d -p 8080:8080 --name gemini zhu327/gemini-openai-proxy:latest
```

必要に応じてポートマッピング（例：`-p 8080:8080`）を調整し、Dockerイメージのバージョン（`zhu327/gemini-openai-proxy:latest`）が要件と一致していることを確認してください。

### Docker-compose版


以下のコマンドを使用してGemini-OpenAI-Proxyを起動します

```bash
docker-compose up
```

---
## 使用方法

Gemini-OpenAI-Proxyは、カスタムOpenAI APIエンドポイントをサポートする任意のアプリケーションにOpenAI機能を統合する簡単な方法を提供します。このプロキシの機能を活用するには、以下の手順に従ってください： 
1. **OpenAIエンドポイントの設定：** 
アプリケーションがカスタムOpenAI APIエンドポイントを使用するように設定されていることを確認してください。Gemini-OpenAI-Proxyは、任意のOpenAI互換エンドポイントとシームレスに動作します。 
2. **Google AI Studio APIキーの取得：** 
プロキシを使用する前に、[ai.google.dev](https://ai.google.dev/)  からAPIキーを取得する必要があります。このAPIキーをGemini-OpenAI-Proxyとやり取りする際のOpenAI APIキーとして扱ってください。 
3. **アプリケーションにプロキシを統合：** 
アプリケーションのAPIリクエストを変更して、取得したGoogle AI Studio APIキーをOpenAI APIキーとして提供するように、Gemini-OpenAI-Proxyをターゲットにしてください。

APIリクエストの例（プロキシが`http://localhost:8080`でホストされていると仮定）：

```bash
curl http://localhost:8080/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $YOUR_GOOGLE_AI_STUDIO_API_KEY" \
 -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
 }'
```



または、Gemini Pro Visionを使用する場合：

```bash
curl http://localhost:8080/v1/chat/completions \
 -H "Content-Type: application/json" \
 -H "Authorization: Bearer $YOUR_GOOGLE_AI_STUDIO_API_KEY" \
 -d '{
     "model": "gpt-4-vision-preview",
     "messages": [{"role": "user", "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
          }
        }
     ]}],
     "temperature": 0.7
 }'
``` 
4. **レスポンスの処理：** 
OpenAIからのレスポンスを処理するのと同じ方法で、Gemini-OpenAI-Proxyからのレスポンスを処理してください。

これで、アプリケーションはOpenAI機能をGemini-OpenAI-Proxyを介して活用できるようになり、OpenAIとGoogle Gemini Proプロトコルを使用するアプリケーションとの間のギャップを埋めます。



## デモスクリプト

### Post Requests

以下は、Gemini-OpenAI-Proxyを使用してOpenAI機能をテストするためのPythonスクリプト例です。あなたのGoogle AI Studio APIキーを設定し、リクエストを送信してレスポンスを確認してください。

#### chat task

`demo/demo_chat.py`

```python
import requests

# あなたのGoogle AI Studio APIキーをここに設定してください
YOUR_GOOGLE_AI_STUDIO_API_KEY = "XXXXXXXXXXXXXXXXXX"

url = "http://localhost:8080/v1/chat/completions"
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
```

#### vision task

`demo\demo_vision.py`

```python
import requests

# あなたのGoogle AI Studio APIキーを再度ここに設定してください
YOUR_GOOGLE_AI_STUDIO_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXX"

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
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                }
            }
        ]
    }],
    "temperature": 0.7
}

response = requests.post(url, json=data, headers=headers)




print(response.text)
```



### OpenAI Python API

`demo/demo_python.ipynb`

#### setting

```python

from IPython.display import display, Image, Audio

import cv2  # We're using OpenCV to read video, to install !pip install opencv-python
import base64
import time
import os
import requests
import openai

YOUR_GOOGLE_AI_STUDIO_API_KEY = "XXXXXXXXXXXXXXXXXXXXXX"

from openai import OpenAI
import httpx
client = OpenAI(api_key = YOUR_GOOGLE_AI_STUDIO_API_KEY)

base_url = httpx.URL("http://localhost:8080/v1/")
client._base_url= base_url

```


#### vision task

```python

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
```

>Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=' The image shows a boardwalk through a lush green field on a bright day with blue skies.', role='assistant', function_call=None, tool_calls=None))

#### chat task

```python

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
```

>ChatCompletionMessage(content="In the realm of code, where logic weaves,\nRecursion's dance, a concept that cleaves.\nA function, bold, within itself it calls,\nTo unravel problems, breaking down their walls.\n\nLike Russian dolls, it delves within,\nEach layer solved, new challenges begin.\nWith grace and skill, it solves its own,\nRevealing patterns, elegantly grown.\n\nA fractal's charm, in code expressed,\nRepeating patterns, echoes intertwined, suggest\nA tapestry of logic, intricate and grand,\nRecursion's power, ever in demand.\n\nFrom sorting lists to solving mazes vast,\nRecursion's touch, a marvel unsurpassed.\nIt climbs the tree, or searches deep,\nIts elegance, a programmer's keep.\n\nYet caution whispers, lest we stray,\nFor infinite loops, a treacherous way.\nWith care we tread, and boundaries define,\nTo tame recursion's power, so divine.\n\nSo let us marvel at this tool so grand,\nRecursion's dance, a symphony unplanned.\nIn the realm of code, it weaves its spell,\nA marvel of logic, stories untold, it tells.", role='assistant', function_call=None, tool_calls=None)


## MEMO

docker network create gemini-openai-proxy-network

(base) E:\Prj\gemini-openai-proxy>docker network ls
NETWORK ID     NAME                             DRIVER    SCOPE
...
cf10300f0f05   gemini-openai-proxy-network      bridge    local
...
