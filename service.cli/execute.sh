#!/bin/sh
# set sh strict mode
set -o errexit
set -o nounset
IFS=$(printf '\n\t')

cd /home/scu/sparcats

echo "starting service as"
echo   User    : "$(id "$(whoami)")"
echo   Workdir : "$(pwd)"
echo "..."
echo
# ----------------------------------------------------------------
# This script shall be modified according to the needs in order to run the service. You can use the inputs in ${INPUT_FOLDER}
# then retrieve the output and move it to the $OUTPUT_FOLDER as defined in the output labels
# For example: cp output.csv $OUTPUT_FOLDER or to $OUTPUT_FOLDER/output.json using jq
# The inputs defined in ${INPUT_FOLDER}/inputs.json are available as env variables by their key in capital letters
# For example: input_1 -> $INPUT_1

# put the code to execute the service here
# For example:
env
ls -al "${INPUT_FOLDER}"
# or for example, to execute a python script on some input data:
env

json_input=$INPUT_FOLDER/inputs.json
    
INPUT_1=$(< "$json_input" jq '.input_1')
export INPUT_1
INPUT_2=$(< "$json_input" jq '.input_2')
export INPUT_2
INPUT_3=$(< "$json_input" jq '.input_3')
export INPUT_3

python3 main.py $INPUT_1 $INPUT_2 $INPUT_3
# cp output_file.json "${OUTPUT_FOLDER}"/output.json

python3 /src/main.py "validation/input_data/input_file.txt"
#cp output_file.json "${OUTPUT_FOLDER}"/output.json

#EOF

