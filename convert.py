import csv
import json

infile = open("mrunali.json", "r")
outfile = open("mrunalione.csv", "w")

writer = csv.writer(outfile)

for row in json.loads(infile.read()):
    for e in row:
        writer.writerow(row)