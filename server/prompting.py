import requests
import json

url = "http://127.0.0.1:5000/chat"
data = {"question": "Qual o propósito do timecode?"}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)