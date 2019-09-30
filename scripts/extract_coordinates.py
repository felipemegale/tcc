import csv

start_locs = []
end_locs = []

with open('csv/uber_peru_2010_formatted_complete_fixed.csv') as in_file:
    reader = csv.reader(in_file, delimiter=';')

    next(reader, None)

    for row in reader:
        start_coord = ((float(row[3]), float(row[4])))
        end_coord = ((float(row[6]), float(row[7])))
        start_locs.append(start_coord)
        end_locs.append(end_coord)

with open('csv/start_coordinates.csv', 'w') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerows(start_locs)

with open('csv/end_coordinates.csv', 'w') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerows(end_locs)