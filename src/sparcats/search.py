# Search tool
# - Search dataset with Experimental Approach. []
# 	- Filter it by organ, sex (Male, Female, & Both)
#
# - Parse each manifest file
# - Separate out each file we need -> We only certain file types (xlsx, csv) - for now
# 	- Filter out certain keywords.
import json
import random

from attr.validators import instance_of
from hurry.filesize import size
from sparc_me import Dataset_Api

from src.sparcats.util import get_algolia_response, traverse_list_of_dict


def get_valid_datasets(exp_approach="electrophysiology", species="mouse", organ="vagus nerve", sex="male"):
    exp_approach = exp_approach.lower()

    # Possible update - match lists
    #if species is None:
    #    animal = ["mouse"]
    #if organ is None:
    #    organ = ["vagus nerve"]

    species = species.lower()
    organ = organ.lower()
    sex = sex.lower()

    dp = Dataset_Api()  # SPARC-ME object
    all_datasets = dp.get_all_datasets_latest_version_pensieve()
    exact_dataset, relevant_datasets = [], []

    i = all_datasets[random.randint(1, 350)]
    j = all_datasets[random.randint(1, 350)]
    k = all_datasets[random.randint(1, 350)]

    exact_dataset_def, relevant_datasets_def = [{'Id': i["id"],
                                                  'Source Dataset Id': i["sourceDatasetId"],
                                                  'Name': i["name"].strip(),
                                                  'Description': i['description'].strip(),
                                                  'Tags': i["tags"],
                                                  'Version': str(i["version"]).strip(),
                                                  "Dataset Size": size(i["size"]),
                                                  "DOI": i["doi"].strip()}], [{'Id': j["id"],
                                                  'Source Dataset Id': j["sourceDatasetId"],
                                                  'Name': j["name"].strip(),
                                                  'Description': j['description'].strip(),
                                                  'Tags': j["tags"],
                                                  'Version': str(j["version"]).strip(),
                                                  "Dataset Size": size(j["size"]),
                                                  "DOI": j["doi"].strip()},
                                                    {'Id': k["id"],
                                                    'Source Dataset Id': k["sourceDatasetId"],
                                                                               'Name': k["name"].strip(),
                                                                               'Description': k['description'].strip(),
                                                                               'Tags': k["tags"],
                                                                               'Version': str(k["version"]).strip(),
                                                                               "Dataset Size": size(k["size"]),
                                                                               "DOI": k["doi"].strip()}
                                                                              ]

    return exact_dataset_def, relevant_datasets_def

    for i in all_datasets:
        response = get_algolia_response(i["id"])
        #response_example = get_algolia_response(375)

        if response is not None:
            if "modalities" in response["item"].keys():
                if exp_approach in traverse_list_of_dict(response["item"]["modalities"], "keyword"):
                    species_match, organ_match, sex_match = False, False, False

                    if species in traverse_list_of_dict(response["organisms"]["subject"]["species"], "name"):
                        species_match = True
                    if species in traverse_list_of_dict(response["organisms"]["subject"]["species"], "name"):
                        species_match = True
                    if sex in traverse_list_of_dict(response["attributes"]["subject"]["sex"], "value"):
                        sex_match = True

                    if species_match and organ_match and sex_match:
                        exact_dataset.append({'Id': i["id"],
                                                  'Source Dataset Id': i["sourceDatasetId"],
                                                  'Name': i["name"].strip(),
                                                  'Description': i['description'].strip(),
                                                  'Tags': i["tags"],
                                                  'Version': str(i["version"]).strip(),
                                                  "Dataset Size": size(i["size"]),
                                                  "DOI": i["doi"].strip()})

                    elif species_match or organ_match or sex_match:
                        relevant_datasets.append({'Id': i["id"],
                                                  'Source Dataset Id': i["sourceDatasetId"],
                                                  'Name': i["name"].strip(),
                                                  'Description': i['description'].strip(),
                                                  'Tags': i["tags"],
                                                  'Version': str(i["version"]).strip(),
                                                  "Dataset Size": size(i["size"]),
                                                  "DOI": i["doi"].strip()})



            #if exp_approach in
            # if "item" in response.keys() and "modalities" in response["item"].keys(): - Seems like an extra check.

        print(i["id"])




def get_all_datasets(exp_app="", organ="", sex=""):
    """Prints a list datasets available on Pensieve.

    Args:

    Return:

    """
    all_datasets = Dataset_Api().get_all_datasets_latest_version_pensieve()

    for i in all_datasets:
        if i["id"] == 429:
            tmp = i
            md = Dataset_Api().get_metadata_pensieve(i["id"], Dataset_Api().get_dataset_latest_version_number(i["id"]))
            print("Pause")

    print("Pause")


if __name__ == "__main__":
    get_valid_datasets()
