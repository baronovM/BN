import requests

url = "https://api.proxyapi.ru/google/v1beta/models/gemini-2.0-flash:generateContent"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer sk-rdLNOdlQVrK4Qxzez8uzBGl9h7AMRXax'
}
data = {
    "contents": [{
        "parts": [{"text": "Привет!"}]
    }]
}

print(requests.post(url, headers=headers, json=data).text)

