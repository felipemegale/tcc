import csv

with open('uber_peru_2010_formatted.csv') as file:
    with open('uber_peru_2010_formatted_complete.csv', 'w') as out_file:
        reader = csv.reader(file, delimiter=';')
        writer = csv.writer(out_file, delimiter=';')

        for row in reader:
            if not (row.count('') > 0):
                writer.writerow(row)
