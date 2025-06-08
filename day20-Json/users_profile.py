import json

people = [
    {"name": "Jeorge", "password": 12345, "email": "george76@gmail.com"},
    {"name": "Ivo", "password": 14332, "email": "ivo67@gmail.com"},
    {"name": "Tisho", "password": 12324, "email": "tisho76@gmail.com"},
    {"name": "Hristo", "password": 43233, "email": "hristo3336@gmail.com"},
    {"name": "Ivan", "password": 14323, "email": "ivandss@gmail.com"}
]

with open("people.json", "w") as f:
    json.dump(people, f)

with open("people.json", "r") as f:
    data = json.load(f)

for email in data:
    print(f"Name: {email['name']} - Email: {email['email']}")

