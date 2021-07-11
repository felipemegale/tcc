'''
ID - guid [1]
Device ID - guid [2]
Vehicle Type - string [3]
Trip Duration - seconds [4]
Trip Distance - meters [5]
Start Time - datetime [6]
End Time - datetime [7]
Modified Date - datetime [8]
Month - number [9]
Hour - number [10]
Day of week - number (Sunday = 0) [11]
Council District (Start) - string [12]
Council District (End) - string [13]
Year - number [14]
Census Tract Start - string [15]
Census Tract End - string [16]
'''

import csv

useful_data = []

with open('csv/dockless_2018.csv', 'r') as r:
    with open('csv/dockless_2018_formatted.csv', 'w') as w:
        fr = csv.reader(r, delimiter=',')
        fw = csv.writer(w, delimiter=',')

        # next(fr, None)

        for row in fr:
            useful_data.append([
                row[1],
                row[4],
                row[5],
                row[6],
                row[7],
                row[11],
                row[12],
                row[13],
                row[15],
                row[16],
            ])
        
        for ud in useful_data:
            fw.writerow(ud)