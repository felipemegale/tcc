#!/bin/bash

aggregated_file="fhvhv_data.csv"
fhvhv_files=`ls ./fhvhv_trip*.csv`

first_file=( $fhvhv_files )

echo "Extracting header..."
head -1 $first_file > $aggregated_file
echo "Extracting header... OK"


for fhvhv_file in $fhvhv_files
do
	echo "Processing $fhvhv_file...";
	tail -n +2 -q $fhvhv_file >> $aggregated_file;
	rm $fhvhv_file;
	echo "Processing $fhvhv_file... OK";
done
