#!/bin/bash

aggregated_file="fhv_data.csv"
fhv_files=`ls ./fhv_trip*.csv`

first_file=( $fhv_files )

echo "Extracting header..."
head -1 $first_file > $aggregated_file
echo "Extracting header... OK"


for fhv_file in $fhv_files
do
	echo "Processing $fhv_file...";
	tail -n +2 -q $fhv_file >> $aggregated_file;
	rm $fhv_file;
	echo "Processing $fhv_file... OK";
done
