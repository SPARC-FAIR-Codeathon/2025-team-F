import sys
import augment

input_data = augment.parse_json()  # Parse the inputs.json file

nb_signals = input_data["nb_signals"]  # Number of augmented signals to create
data = augment.read_from_csv("../../validation/input/test.csv")
arr_augmenters = augment.setup_augmenter(input_data)
augmenter = augment.create_augmenter(arr_augmenters)

augmented_data = augment.generate_augmented_data(data, augmenter, nb_signals)
augment.save_to_csv(augmented_data, 1, "augmented_data.csv")
