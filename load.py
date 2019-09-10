import json
import csv

# datastore =open("mrunali.json").read()
# json_load = json.loads(datastore)
# print(datastore)
#

with open('mrunali.json','r') as f:
    distros_dict = json.load(f)


outF = open("myoutfile.csv", "w")
writer = csv.writer(outF)
for distro in distros_dict:
    writer.writerows(distro)