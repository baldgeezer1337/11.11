
people_string='''
{
    "people":[
        {
    "name":"Ann Smith",
    "phone": 28499543,
    "emails": ["ann2@gmail.com", "ann.smith@gmail.com"]
    },
    {
    "name":"Tom Brown",
    "phone": 26349012,
    "emails": ["tomasssss@gmail.com", "tomtom@gmail.com"]
    }
    ]}
'''

import json
data=json.loads(people_string)
print(data)
print(data['people'])