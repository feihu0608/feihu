# curl -X POST 'https://api.dify.ai/v1/workflows/run' \
# --header 'Authorization: Bearer {api_key}' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#   "inputs": {},
#   "response_mode": "streaming",
#   "user": "abc-123"
# }'

import requests

res = requests.post(
    url='https://api.dify.ai/v1/workflows/run',
    headers={'Authorization': 'Bearer app-p6NQJ5aqurSDpUgsKdxzXNn3',"Content-Type": "application/json"},
    json={
        "inputs":{
            "feedback":"我的电脑起飞了"
        },
        "response_mode":"streaming", # blicking常用streaming
        "user": "heihei"
    }
)

# print(res.text)


print(type(res))
for item in res.iter_lines():
    if item:
        print(item)
