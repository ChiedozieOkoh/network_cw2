import re

logFile = "testing.log"

important = []
keep_phrases = ["packets", "rtt"]

with open(logFile) as f:
    f = f.readlines()

for line in f:
    for phrase in keep_phrases:
        if phrase in line:
            important.append(line)
            break

print(important)

pattern = r"(?:\d+(?:\.\d+)?%|/\d+(?:\.\d+)?|\d+(?:\.\d+)?(?=%|/|$))"
matches = []

for text in important:
    matches.extend(re.findall(pattern, text))

numbers = [
    float(x.replace("/", "")) if "/" in x else float(x.rstrip("%")) for x in matches
]

nums = []
for x in numbers:
    nums.append(float(x))

print(nums)
