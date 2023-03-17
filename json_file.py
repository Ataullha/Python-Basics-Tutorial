phonebook = {}

phonebook['tom'] = {
    'name': 'Mr. Thomas',
    'address': 'NY',
    'phone': 1234
}

phonebook['jerry'] = {
    'name': 'Mr. Jerry',
    'address': 'NJ',
    'phone': 5678
}

# print(phonebook)

import json

s = json.dumps(phonebook)
print(s)



import json

with open('phonebook.txt', 'w') as f:
    f.write(s)

with open('phonebook.txt', 'r') as f:
    s = f.read()

# print(s)

# load that file as a dict
txt = json.loads(s)

print(txt)

for perons, info in txt.items():
    print(perons, info)