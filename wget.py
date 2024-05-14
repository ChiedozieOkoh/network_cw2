import csv
import re
import numpy
from datetime import datetime

logFile = "wgettest.log"

data = []
domains = []
times = []
keep_phrases = ["B/s", "Length"]
domain_phrases = ["http"]
timestamps = ["timestamp"]

with open(logFile) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            data.append(line)
            break
    for phrase in domain_phrases:
        if phrase in line:
            domains.append(line)
            break
    for phrase in timestamps:
        if phrase in line:
            times.append(line)
            break

pattern = r"\((.*?)\)"

print("Domains", domains)

matches = []

for text in data:
    matches.extend(re.findall(pattern, text))

domainnames = []
timesstrs = []
for line in domains:
    x = line.split()
    timesstrs.append(x[0].replace("--", "") + " " + x[1].replace("--", ""))
    domainnames.append((x[2]))

print("TIMESADWD", timesstrs)

# finaltimes = []
# for x in timesstrs:
#     finaltimes.append(datetime.strptime(x, "%y-%m-%d %H:%M:%S"))


# timenums = []
# for text in times:
#     timenums.extend(re.findall(r"\d+", text))
#
# finaltimes = []
# for x in timenums:
#     x = int(x)
#     y = datetime.fromtimestamp(x)
#     print(y)
#     finaltimes.append(y)
#
# print("TIMES", finaltimes)

# print("DATES", finaltimes)


print("names", (domainnames))
print(matches)

numbers = []
for text in matches:
    scale = 1
    if "M" in text:
        scale = 1024
    num = re.findall(r"([-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?)", text)
    number = float(num[0]) * scale
    numbers.append(number)


print(numbers)

counter = 0
longlist = []
# shortlist = []
for i in range(0, len(domainnames)):
    # shortlist = domainnames[i] + timesstrs[i] + numbers[counter] + numbers[counter + 1]
    shortlist = []
    shortlist.append(domainnames[i])
    shortlist.append(timesstrs[i])
    shortlist.append(numbers[counter])
    shortlist.append(numbers[counter + 1])
    counter += 2
    longlist.append(shortlist)


list = numpy.array(longlist)
list = list.reshape(-1, 4)

fields = ["host", "time", "speed", "size"]

filename = "wgettest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(list)
