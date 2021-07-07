import csv

with open('csv/dockless_2018_formatted.csv', 'r') as r:
    with open('csv/dockless_2018_formatted_complete.csv', 'w') as w:
        fr = csv.reader(r, delimiter=',')
        fw = csv.writer(w, delimiter=',')

        for row in fr:
            if not (row.count('') > 0):
                fw.writerow(row)