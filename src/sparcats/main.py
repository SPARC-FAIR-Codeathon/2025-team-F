import sys
import augment
import warnings
import pathlib

input_data = augment.parse_json(sys.argv[1])  # Parse the inputs.json file

nb_signals = input_data["nb_signals"]  # Number of augmented signals to create

# Read input data
for filepath in input_data["source_data_files"]:

    if filepath.endswith('.csv'):
        data = augment.read_from_csv(filepath)
    elif filepath.endswith('.mat'):
        data = augment.read_from_mat(filepath)
    else:
        warnings.warn(f"Unsupported file type for {filepath}. Supported types are .csv and .mat.")

arr_augmenters = augment.setup_augmenter(input_data)
augmenter = augment.create_augmenter(arr_augmenters)

augmented_data = augment.generate_augmented_data(data, augmenter, nb_signals)
augment.save_to_csv(augmented_data, 1, "augmented_data.csv")
