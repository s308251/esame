#!/bin/bash

wget https://raw.githubcontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
if [ $? -eq 0 ]
    then 
        echo OK
    else
        echo FAULT
fi
ls -l Nemo_6670.dat

SCRIPT_PATH=$(cd "$(dirname "$0")" && pwd)
DATA_FILE_PATH="$SCRIPT_PATH/Nemo_6670.dat"
export DATA_FILE_PATH
echo $DATA_FILE_PATH


python3 python_esame_Papini.py "$DATA_FILE_PATH"

