import csv
import re

logFile = "testing.log"

input = []
keep_phrases = ["packets", "rtt"]

with open(logFile) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            input.append(line)
            break

print(input)

pattern = r"(?:\d+(?:\.\d+)?%|/\d+(?:\.\d+)?|\d+(?:\.\d+)?(?=%|/|$))"
matches = []

for text in input:
    matches.extend(re.findall(pattern, text))

numbers = [
    float(x.replace("/", "")) if "/" in x else float(x.rstrip("%")) for x in matches
]

nums = []
for x in numbers:
    nums.append(float(x))

print(nums)

fields = ["packet loss %", "rttMin", "rttavg", "rttMax", "rttmdev"]

# convert nums array to 2d array
list = [nums[i : i + 5] for i in range(0, len(nums), 5)]

# print(data)

filename = "pingtest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(list)
