#!/bin/bash
echo 'CREATING BLOCKS FOR SORTING..........'
mkdir temp
./blocks


for file in ~/temp/*; do
  #echo ${file##*/}
  echo 'Accessing file ' ${file##*/}	
  ./sort ${file##*/}
done	