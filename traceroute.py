import csv
import re

logFile = "routetest.log"

data = []
with open(logFile) as f:
    f = f.readlines()

for line in f:
    data.append(line)

# print(data)
list = []
superlist = []
for x in data:
    x = x.strip("\n")
    if x[0].isdigit() or x[0] == " ":
        list.append(x)
    else:
        superlist.append(list)
        list = []

        # get name and ip
        names = x.split(" ")
        x = names[2] + names[3]
        list.append(x)


print(superlist)


fields = ["host/trip", "ip" "times"]

filename = "traceroutetest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(superlist)
