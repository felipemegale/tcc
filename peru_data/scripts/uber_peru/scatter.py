import gmplot
import pandas as pd

gmap_start = gmplot.GoogleMapPlotter(-12.054828, -77.066767, 11)
gmap_end = gmplot.GoogleMapPlotter(-12.054828, -77.066767, 11)

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=';')

start_lats = trips['start_lat'].tolist()
start_lons = trips['start_lon'].tolist()

end_lats = trips['end_lat'].tolist()
end_lons = trips['end_lon'].tolist()

gmap_start.scatter(start_lats, start_lons, '#FFFF00', size=3, marker=False)
gmap_start.draw("maps/start_scatter.html")

gmap_end.scatter(end_lats, end_lons, '#FFFF00', size=3, marker=False)
gmap_end.draw("maps/end_scatter.html")
