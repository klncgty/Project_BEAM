#searching our document  with id 

import requests
import json
import textwrap
id = "64ca0a7b-2604-42dc-b22e-e54204ebb96d"  

api_key= "tnt_4WSmhOgJPa7_cPe3bsvKs8Jp8ZVpZKiFQYImxzOWpYUR1ztfK9A7MI"

url = f"https://api.ragie.ai/documents/{id}"
headers = {"Authorization": f"Bearer {api_key}"}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  

    data = response.json()
    pretty_json = json.dumps(data, indent=4)
    wrapped_text = textwrap.fill(pretty_json, width=190)
    print(wrapped_text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")