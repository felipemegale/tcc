import csv


def fix_number(number):
    return number.replace(',', '.', 1)


fixed_list = []

with open('csv/uber_peru_2010_formatted_complete.csv') as file:
    reader = csv.reader(file, delimiter=';')

    for row in reader:
        fixed_list.append(
            [row[0], row[1], fix_number(row[2]), fix_number(row[3]), row[4], fix_number(row[5]), fix_number(row[6]), fix_number(row[7])])

with open('csv/uber_peru_2010_formatted_complete_fixed.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')

    for row in fixed_list:
        writer.writerow(row)
