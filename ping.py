import csv
import re
from datetime import datetime

logFile = "pingtest2.log"

data = []
domains = []
times = []
keep_phrases = ["packets", "rtt"]
domain_phrases = ["ping"]
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

# print(data)
print("TIMES", times)

pattern = r"(?:\d+(?:\.\d+)?%|/\d+(?:\.\d+)?|\d+(?:\.\d+)?(?=%|/|$))"

domain_names = []
matches = []

for text in domains:
    arr = text.split()
    domain_names.append(arr[1])

print(domain_names)
for text in data:
    matches.extend(re.findall(pattern, text))

numbers = [
    float(x.replace("/", "")) if "/" in x else float(x.rstrip("%")) for x in matches
]

timenums = []
for text in times:
    timenums.extend(re.findall(r"\d+", text))

finaltimes = []
for x in timenums:
    x = int(x)
    y = datetime.fromtimestamp(x)
    print(y)
    finaltimes.append(y)


# every 20 items add time

print(finaltimes)

nums = []
counter1 = 0
counter2 = 5
counter3 = 3
for x in numbers:
    # print("1", counter1)
    if counter2 == 5:
        nums.append(domain_names[counter1])
        print("counter dawd", counter1 // 4)
        nums.append(finaltimes[counter1 // 4])
        counter1 += 1
        counter2 = 0
    nums.append(float(x))
    counter2 += 1

# print(nums)

fields = ["host", "time", "packet loss %", "rttMin", "rttavg", "rttMax", "rttmdev"]

# convert nums array to 2d array
list = [nums[i : i + 7] for i in range(0, len(nums), 7)]

list.sort()


filename = "pingtest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(list)
