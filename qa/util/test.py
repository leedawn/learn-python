import requests

test_url="http://127.0.0.1:8001/games/"
result=requests.get(test_url)
print(result.text)