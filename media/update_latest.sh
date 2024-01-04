#! /bin/bash

if [ -f ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ Ties.csv ]
then
	mv ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ Ties.csv ./ties.csv
	python3 convert_ties.py
fi


# if newly-downloaded media list)
if [ -f ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ In\ the\ Media.csv ]
then
	rm ./news.csv
	(tail -n +2 ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ In\ the\ Media.csv) >> news.csv
	rm ~/Downloads/UK\ Mapping\ Fossil\ Ties\ Database\ -\ In\ the\ Media.csv
	python3 get_metadata.py
fi



cp ties.json ../src/assets/
cp news.json ../src/
