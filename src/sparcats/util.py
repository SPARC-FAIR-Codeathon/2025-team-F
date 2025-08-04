import requests

algolia_app_key = "97dd61c1688581bfee8f74e7e4739758"
algolia_app_id = "04WW1V1O0F"


def get_algolia_response(datasetId):
    url = f"https://04WW1V1O0F-dsn.algolia.net/1/indexes/SPARC_pr/{datasetId}"

    custom_headers = {
        'X-Algolia-API-Key': algolia_app_key,
        'X-Algolia-Application-Id': algolia_app_id,
        'Content-Type': 'application/json',
    }

    # Make a GET request with headers
    try:
        response = requests.get(url, headers=custom_headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Response text: {response.text}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def traverse_list_of_dict(val, key="keyword"):
    output = []
    for i in val:
        output.append(i[key].lower())
    return output
