#!/bin/bash



for file in ~/temp/tf/calc/final/*; do
  #echo ${file##*/}
  echo 'Accessing file ' ${file##*/}	
  ./calc_idf ${file##*/}
done	
