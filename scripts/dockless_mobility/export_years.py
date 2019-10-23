import pandas as pd

print("reading file...")
trips = pd.read_csv(
    "../../Downloads/Shared_Micromobility_Vehicle_Trips-10-22-2019.csv", low_memory=False)
print("reading file... OK")

print("querying dataframe...")
trips_2019 = trips.loc[trips['Year'] == 2019]
print("querying dataframe... OK")

print("exporting dataframe...")
trips_2019.to_csv('csv/dockless_2019.csv')
print("exporting dataframe... OK")
