import requests

BASE = "http://127.0.0.1:5000"

response = requests.put(BASE + "/Name/Lucas", {"age": 12, "gender": "male"})
response2 = requests.get(BASE + "/Name/Andy")

print(response.json())
print(response2.json())