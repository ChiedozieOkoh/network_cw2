import csv
import re

logFile = "testing.log"

data = []
domains = []
keep_phrases = ["packets", "rtt"]
domain_phrases = ["ping"]

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

# print(data)

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

print(numbers)

nums = []
counter1 = 0
counter2 = 5
for x in numbers:
    print("1", counter1)
    if counter2 == 5:
        nums.append(domain_names[counter1])
        counter1 += 1
        counter2 = 0
    nums.append(float(x))
    counter2 += 1

# print(nums)

fields = ["host", "packet loss %", "rttMin", "rttavg", "rttMax", "rttmdev"]

# convert nums array to 2d array
list = [nums[i : i + 6] for i in range(0, len(nums), 6)]


filename = "pingtest.csv"

with open(filename, "w") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(fields)
    writer.writerows(list)
