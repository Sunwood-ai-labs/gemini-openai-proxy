import requests

# あなたのGoogle AI Studio APIキーをここに設定してください
YOUR_GOOGLE_AI_STUDIO_API_KEY = "AIzaSyA6SW3VQhYkHZhDJpU2kfHf15ATH9lYwTE"

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