import csv
import re
import numpy

logFile = "wgettest.log"

data = []
keep_phrases = ["B/s", "Length"]

with open(logFile) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            data.append(line)
            break

pattern = r"\((.*?)\)"

matches = []

for text in data:
    matches.extend(re.findall(pattern, text))

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

list = numpy.array(numbers)
list = list.reshape(-1, 2)

fields = ["speed", "size"]

filename = "wgettest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(list)
