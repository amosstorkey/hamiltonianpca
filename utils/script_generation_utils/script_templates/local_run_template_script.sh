#!/bin/sh

cd ../../
export DATASET_DIR="datasets/"
# Activate the relevant virtual environment:
python $execution_script$ --config experiment_files/experiment_config_files/$experiment_config$ "$@"
