import csv

useful_data = []

with open('uber_peru_2010.csv') as file:
    with open('uber_peru_2010_formatted.csv', 'w') as out_file:
        reader = csv.reader(file, delimiter=';')
        writer = csv.writer(out_file, delimiter=';')

        for row in reader:
            useful_data.append(
                [row[1], row[6], row[7], row[8], row[9], row[10], row[11]])

        for data in useful_data:
            writer.writerow(data)
