import json
person = '{"Name": "Tiger Nixon", "Position": "System Architect"}'
person_dict = json.loads(person)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print( person_dict)
# Output: ['English', 'French']
print(person_dict['Position'])