#!/bin/bash



for file in ~/temp/tf/*; do
  #echo ${file##*/}
  echo 'Accessing file ' ${file##*/}	
  python stem.py ${file##*/}
done	
