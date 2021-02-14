import requests

response = requests.get("https://randomfox.ca/floof")
print(response.status_code)