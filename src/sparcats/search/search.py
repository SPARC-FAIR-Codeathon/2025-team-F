import os

from sparc_me import Dataset_Api

from src.sparcats.search.util import get_algolia_response, tags_exists, traverse_list_of_dict

dp = Dataset_Api()  # SPARC-ME object


# Warning: May take a minute or two to run, as well of the datasets in pensieve are being checked.
def get_valid_datasets(exp_approach="electrophysiology", species="mouse", organ="vagus nerve", sex="both"):
    exp_approach = exp_approach.lower()

    # (Future) TODO: - match lists i.e. multiple species and organs.
    #if species is None:
    #    animal = ["mouse"]
    #if organ is None:
    #    organ = ["vagus nerve"]

    species = species.lower()
    organ = organ.lower()
    sex = sex.lower()

    all_datasets = dp.get_all_datasets_latest_version_pensieve()
    exact_dataset, relevant_datasets = "", ""

    for i in all_datasets:
        response = get_algolia_response(i["id"])

        if response is not None:
            if tags_exists(response, ["item", "modalities", "keyword"]):
                if exp_approach in traverse_list_of_dict(response["item"]["modalities"], "keyword"):
                    species_match, organ_match, sex_match = False, False, False

                    # Double traversing as the tag contains lists of dictionaries within a list of dictionaries.
                    # Each species have their own list.
                    species_tag = []
                    if tags_exists(response, ["organisms", "subject", "species", "name"]):
                        species_tag = traverse_list_of_dict(traverse_list_of_dict(response["organisms"]["subject"],
                                                                                  "species"), "name")

                    if species in species_tag:
                        species_match = True
                    if (tags_exists(response, ["anatomy", "organ", "name"])
                            and organ in traverse_list_of_dict(response["anatomy"]["organ"], "name")):
                        organ_match = True
                    if tags_exists(response, ["attributes", "subject", "sex", "value"]):
                        sex_tags = traverse_list_of_dict(response["attributes"]["subject"]["sex"], "value")
                        if sex == "both" and "male" in sex_tags and "female" in sex_tags:
                            sex_match = True
                        elif sex in sex_tags:
                            sex_match = True

                    if species_match and organ_match and sex_match:
                        if exact_dataset == "":
                            exact_dataset = str(i["id"])
                        else:
                            exact_dataset = exact_dataset + "," + str(i["id"])

                    elif species_match or organ_match or sex_match:
                        if relevant_datasets == "":
                            relevant_datasets = str(i["id"])
                        else:
                            relevant_datasets = relevant_datasets + "," + str(i["id"])

    return exact_dataset, relevant_datasets
