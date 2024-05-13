import csv
import re

logFile = "routetest.log"

data = []
list = []
with open(logFile) as f:
    f = f.readlines()

for line in f:
    data.append(line)

for x in data:
    x = x.strip("\n")
    if x[0].isdigit() or x[0] == " ":
        x = x.replace("ms", "")
        str = x.split()
        list.append(str)
    else:
        # get name and ip
        names = x.split(" ")
        x = names[2] + names[3]
        print(x)
        namesList = []
        namesList.append(x)
        list.append(namesList)

print(list)

fields = ["host/trip", "ip", "times"]

filename = "traceroutetest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(list)
