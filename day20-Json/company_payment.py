import json

people_company = [
    {"name": "Ivo", "Salary": 3500},
    {"name": "John", "Salary": 2500},
    {"name": "Rita", "Salary": 4000},
    {"name": "Back", "Salary": 2000},
    {"name": "Brenden", "Salary": 5500},
]

with open("salary.json", "w") as f:
    json.dump(people_company, f)

with open("salary.json", "r") as f:
    data = json.load(f)

for payment in data:
    if payment['Salary'] > 3000:
        print(f"Name: {payment['name']} with salary: {payment['Salary']}")