from calcs import calculate_distance_between_positions, calculate_time_difference_in_milliseconds
import networkx
import csv


trips = []

with open('csv/uber_peru_2010_formatted_complete_fixed.csv') as trip_file:
    reader = csv.reader(trip_file, delimiter=";")

    # load to memory the trips from the file
    for row in reader:
        trips.append(row)
