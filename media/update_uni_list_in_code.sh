#! /bin/bash

if [ -f ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ List\ of\ unis\ for\ overview\ -\ in\ progress.csv ]
then
	mv ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ List\ of\ unis\ for\ overview\ -\ in\ progress.csv ./uniList.csv
fi


python3 generate_uni_list_in_code.py


