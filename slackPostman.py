import requests
import json
import secret

def send(message):
    
    payload = {'text': message}

    requests.post(
        secret.webhook_url, data = json.dumps(payload),
        headers = {'Content-Type': 'application/json'}
        )
