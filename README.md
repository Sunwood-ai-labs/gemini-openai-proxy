<h1>
<img src="https://raw.githubusercontent.com/Sunwood-ai-labs/gemini-openai-proxy/main/docs/geminicat.png" height=300px align="right"/>
Gemini-OpenAI-Proxy
</h1>

Gemini-OpenAI-Proxyは、OpenAI APIプロトコルをGoogle Gemini Proプロトコルに変換するためのプロキシです。これにより、Gemini Proプロトコルを使用するアプリケーションにOpenAIが提供する機能をシームレスに統合することが可能になります。



---


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

以下は、Gemini-OpenAI-Proxyを使用してOpenAI機能をテストするためのPythonスクリプト例です。あなたのGoogle AI Studio APIキーを設定し、リクエストを送信してレスポンスを確認してください。

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
