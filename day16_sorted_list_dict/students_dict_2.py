students = [
{"name": "Ivan", "grade": 75},
{"name": "Ivo", "grade": 65},
{"name": "Jony", "grade": 57},
{"name": "Rado", "grade": 95},
{"name": "Rozy", "grade": 15},
]

stud_sort = sorted(students, key=lambda x: x["grade"])

for student in stud_sort:
    print(student["name"], student["grade"])