import pandas as pd
from matplotlib import pyplot as plt
import math

trips = pd.read_csv("csv/uber_peru_2010_formatted_complete_fixed.csv", sep=";")
users = trips["user_id"].tolist()
user_trip_count = {}

for user in users:
    try:
        user_trip_count[user] += 1
    except:
        user_trip_count[user] = 1

# each position in this list represents, for example, that 416 people traveled 1 time
# i.e. position 1 hold 416
trip_count = [list(user_trip_count.values()).count(i)
              for i in range(max(user_trip_count.values()))]

plt.figure(figsize=(7.3, 5.5))
plt.bar([i for i in range(len(trip_count))], [
        val for val in trip_count], width=1.6, color="xkcd:azure")
plt.title("Ride count by user count")
plt.xlabel("Ride count")
plt.ylabel("User count")
plt.savefig("images/ride_by_user.png")
