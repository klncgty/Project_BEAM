### uploading and processing on ragie. 
import os
import json
from requests import post, exceptions

api_key = "tnt_2DYrMSogwqi_Wkezkg3VyLWJJP0JcH8kleQ6InzrbF1eITbfNcs8OSx"
file_path = "all_tables.json"
                                                                
try:
    with open(file_path, "rb") as f:
        print("file found")
        content = f.read()
except FileNotFoundError:
    print(f"Dosya bulunamadı: {file_path}")
    exit()

metadata = {"title": "all_tables", "environment": "json_source"}

data = {
    "metadata": json.dumps(metadata)
}

files = { "file": (file_path, content), }

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json"
}

try:
    response = post("https://api.ragie.ai/documents", data=data, files=files, headers=headers)
    response.raise_for_status()  
    print("File uploaded successfully!")
except exceptions.RequestException as e:
    print(f"Uploading error: {e}")
