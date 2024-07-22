import requests
import json

url = 'http://localhost:3000/secret'

answer = {
    "password": "MONaNa"
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url, headers=headers, data=json.dumps(answer))

if response.status_code == 200 and response.json().get('status') == 'success':
    print(response.text)
else:
    print(response.text)
    exit()