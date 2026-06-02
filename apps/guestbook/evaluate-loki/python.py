import requests
import time

# Loki push endpoint
url = "http://localhost:3100/loki/api/v1/push"

# Current time in nanoseconds (string format)
curr_time = str(time.time_ns())

payload = {
    "streams": [
        {
            "stream": {
                "job": "python-app",
                "environment": "testing",
                "level": "error"
            },
            "values": [
                [curr_time, "ERROR: Database connection timeout on retry 3."]
            ]
        }
    ]
}

headers = {'Content-type': 'application/json'}
response = requests.post(url, json=payload, headers=headers)
print(f"Log sent! Response status: {response.status_code}")