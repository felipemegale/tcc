import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np

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
        val for val in trip_count], color="xkcd:azure", width=0.6)
plt.title("Ride count by user count")
plt.xlabel("Ride count (log)")
plt.ylabel("User count (log)")
plt.xscale("log")
plt.yscale("log")

x_values = plt.xticks()
y_values = plt.yticks()
x_values = [x_values[0][val] for val in range(len(y_values[0]))]

coef = np.polyfit(x_values, y_values[0], 1)
poly1d_fn = np.poly1d(coef)

plt.plot(x_values, y_values[0], 'yo',
         x_values, poly1d_fn(x_values), '--k')
plt.show()
# plt.savefig("images/ride_by_user_log_log.png")
# plt.show()
