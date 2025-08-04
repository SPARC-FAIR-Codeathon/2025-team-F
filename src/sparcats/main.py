import search
import util
import json
import sys

# get url(?) to the rleevant data files
(exact_datasets, relevant_datasets) = search.get_valid_datasets(input_form[sys.argv[1]], input_form[sys.argv[2]],input_form[sys.argv[3]])

outfile_exact = "output_exact.json"
with open('config.json', 'w') as outfile:
    json.dump(exact_datasets, outfile)

outfile_relevant = "output_relevant.json"
with open('config.json', 'w') as outfile:
    json.dump(relevant_datasets, outfile)

