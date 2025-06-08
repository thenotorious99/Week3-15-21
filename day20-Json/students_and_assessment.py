import json

students = [
    {"name": "Ivan", "assessment": 6},
    {"name": "Radi", "assessment": 4},
    {"name": "Iovan", "assessment": 5},
    {"name": "Tisho", "assessment": 6}
]

with open("students.json", "w") as f:
    json.dump(students, f)

with open("students.json", "r") as f:
    data = json.load(f)

for row in data:
    if row["assessment"] > 5:
        print(row["name"])