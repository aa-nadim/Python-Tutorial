import requests
import pprint

url = "http://127.0.0.1//rest/v1/vlans"

get_vlans = requests.get(url)

get_vlans_json = get_vlans.json()

print(type(get_vlans_json))

pprint.pprint(get_vlans.json)