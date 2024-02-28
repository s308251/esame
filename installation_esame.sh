#!/bin/bash

#creare directory dove copiare applicazione
mkdir -p dir_esame

#copiare lo start_script bash e il file python in opportuni path
cp download_dati.sh  dir_esame/
cp python_esame_Papini.py  dir_esame/



# attribuire i permessi d'esecuzione corretti

chmod a+x installation_esame.sh
chmod a+rx download_dati.sh
chmod a+rx python_esame_Papini.py

#lancio script di esecuzione
./download_dati.sh




