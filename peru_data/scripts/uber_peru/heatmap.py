import gmplot
import csv
  
start_lats = []
start_longs = []
end_lats = []
end_longs = []

with open('csv/start_coordinates.csv') as start_coords:
    reader = csv.reader(start_coords, delimiter=';')

    for row in reader:
        start_lats.append(float(row[0]))
        start_longs.append(float(row[1]))

with open('csv/end_coordinates.csv') as end_coords:
    reader = csv.reader(end_coords, delimiter=';')
    
    for row in reader:
        end_lats.append(float(row[0]))
        end_longs.append(float(row[1]))

gmap_start = gmplot.GoogleMapPlotter(-12.054828, -77.066767, 11)
gmap_end = gmplot.GoogleMapPlotter(-12.054828, -77.066767, 11)

gmap_start.heatmap(start_lats, start_longs)
gmap_end.heatmap(end_lats, end_longs)

gmap_start.draw("/home/felipe/repositories/tcc/maps/start_heatmap.html")
gmap_end.draw("/home/felipe/repositories/tcc/maps/finish_heatmap.html")