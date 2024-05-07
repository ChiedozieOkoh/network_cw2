import csv

data = [
    {"ip": "172.217.16.238", "ttl": "57", "time": "17.8"},
    {"ip": "172.217.16.238", "ttl": "57", "time": "16.5"},
    {"ip": "172.217.16.238", "ttl": "57", "time": "16.4"},
    {"ip": "172.217.16.238", "ttl": "57", "time": "16.1"},
    {"ip": "172.217.16.238", "ttl": "57", "time": "16.1"},
    {"ip": "172.217.16.238", "ttl": "57", "time": "15.9"},
    {"ip": "172.217.16.238", "ttl": "57", "time": "16.0"},
]

fields = ["ip", "ttl", "time"]

filename = "pingtest.csv"

with open(filename, "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(data)
