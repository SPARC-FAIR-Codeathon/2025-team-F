import sys
import augment_service as augment
import warnings
import pathlib
import os

# In osparc, INPUT_FOLDER and OUTPUT_FOLDER are environment variables 
# that map to the service input/output ports, respectively
input_dir = os.environ["INPUT_FOLDER"] 
output_dir = os.environ["OUTPUT_FOLDER"]
input_data = augment.parse_json(input_dir + "/input_form.json")
print("?????")
print(input_data)

nb_signals = input_data["nb_signals"]  # Number of augmented signals to create

# Read input data
for filepath in input_data["source_data_files"]:

    if filepath.endswith('.csv'):
        data = augment.read_from_csv(input_dir + "/" + filepath)
    elif filepath.endswith('.mat'):
        data = augment.read_from_mat(input_dir + "/" + filepath)
    else:
        warnings.warn(f"Unsupported file type for {filepath}. Supported types are .csv and .mat.")

arr_augmenters = augment.setup_augmenter(input_data)
augmenter = augment.create_augmenter(arr_augmenters)

augmented_data = augment.generate_augmented_data(data, augmenter, nb_signals)
augment.save_to_csv(augmented_data, 1, output_dir + "augmented_data.csv")