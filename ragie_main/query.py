# vector search-query func.
import json
import requests
import textwrap

def ask_ragie(test_data):   
    filter_data = {"environment": "hires"}

    data = {"query": test_data, "filter": filter_data,"rerank": True, "top_k": 1}
    body = json.dumps(data)

    url = "https://api.ragie.ai/retrievals"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    try:
    
        response = requests.post(url, headers=headers, data=body)
        response.raise_for_status()  

        data = response.json()
        #print(data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    text_list = [chunk['text'] for chunk in data['scored_chunks']]
    combined_text = '\n'.join(text_list)
    wrapped_text  = textwrap.wrap(combined_text, width=100)
    return wrapped_text

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  
    test_data = "YOUR_TEST_QUERY"  

    result = ask_ragie(test_data)

    if result:
        for line in result:
            print(line)