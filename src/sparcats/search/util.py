import os

import requests
from dotenv import load_dotenv


def get_algolia_response(datasetId):
    load_dotenv(dotenv_path="../../config/.env")
    url = f"https://04WW1V1O0F-dsn.algolia.net/1/indexes/SPARC_pr/{datasetId}"

    custom_headers = {
        'X-Algolia-API-Key': os.getenv("ALGOLIA_APP_KEY"),
        'X-Algolia-Application-Id': os.getenv("ALGOLIA_APP_ID"),
        'Content-Type': 'application/json',
    }

    # Make a GET request with headers
    try:
        response = requests.get(url, headers=custom_headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.json()
        else:
            #print(f"[Warning]: Request failed with status code: {response.status_code} for datasetId: {datasetId}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"[Error] An error occurred while fetching data for datasetId [{datasetId}]. "
              f"Below are the details of the error: {e}")


def traverse_list_of_dict(val, key="keyword"):
    output = []
    for i in val:
        if key in i.keys():  # Added to ignore tags that are not required.
            if isinstance(i[key], dict):
                output.append(i[key])
            else:
                output.append(i[key].lower())
    return output


# List of tags to be checked in hierarchy
def tags_exists(val, tags):
    key = tags.pop(0)
    if key in val.keys():
        if len(tags) > 0:
            if isinstance(val[key], dict):
                return tags_exists(val[key], tags)
            elif isinstance(val[key], list):
                return tags_exists(val[key][0],
                                   tags)  # Only checking one element of the list. Assumption all items under the tag will have similar tags.
        return True
    else:
        return False
