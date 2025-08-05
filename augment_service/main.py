
import json
import matplotlib.pyplot as plt
import numpy as np
import os

# In osparc, INPUT_FOLDER and OUTPUT_FOLDER are environment variables 
# that map to the service input/output ports, respectively
input_dir = os.environ["INPUT_FOLDER"] 
output_dir = os.environ["OUTPUT_FOLDER"]

# load opencor output
with open(os.path.join(input_dir, 'output_data.json')) as f:
    data = json.load(f)
    

fig, ax = plt.subplots(nrows=2, ncols=1, sharex='all')

# plot opencor output
ax[0].plot(np.array(data["Time/time"])/1000, data["neural_input/f_i"]*(np.array(data["neural_input/w_iICC"])>0), 'r')
ax[0].plot(np.array(data["Time/time"])/1000, data["neural_input/f_e"]*(np.array(data["neural_input/w_e"])>0), 'b')
ax[0].legend(['Inhibitory', 'Excitatory'])
ax[1].plot(np.array(data["Time/time"])/1000, data["active_tension/T"], 'k')
plt.xlabel("Time (s)")
ax[0].set_ylabel("Stimulation frequency (Hz)")
ax[1].set_ylabel("Tension (kPa)")

ax[0].set_ylim(-0.1, 10.1)
ax[1].set_ylim(0, 75)

# replace my_output_file.txt with name of choice
outputfile = "output_tension_figure.png" 
outputfile_name = os.path.join(output_dir, outputfile)

# save figure
fig.savefig(outputfile_name)

# # Trying to see if I can access data from another input

# outputfile = "output_directories.txt" 
# outputfile_name = os.path.join(output_dir, outputfile)

# sourceFile = open(outputfile_name, 'w+')
# print(f'input: {input_dir}; output: {output_dir}', file=sourceFile)
# abc = os.listdir(input_dir)
# print(abc, file=sourceFile)
# xyz = os.listdir(input_dir+ '/..')

# print(xyz, file=sourceFile)
# with open(os.path.join(input_dir, 'inputs.json')) as f:
    # readfile = f.readlines()
    # print(readfile, file=sourceFile)


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
augment.save_to_csv(augmented_data, 1, output_dir + "augmented_data.csv")