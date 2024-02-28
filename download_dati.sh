#!/bin/bash

wget https://raw.githubcontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat
if [ $? -eq 0 ]
    then 
        echo OK
    else
        echo FAULT
fi
ls -l Nemo_6670.dat

export DATA_FILE_PATH='pwd'//Nemo_6670.dat
echo $DATA_FILE_PATH



python3 Python_esame_Papini.py "$DATA_FILE_PATH"
