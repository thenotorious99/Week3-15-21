students = [
{"name": "Ivan", "grade": 75},
{"name": "Ivo", "grade": 65},
{"name": "Jony", "grade": 57},
{"name": "Rado", "grade": 95},
{"name": "Rozy", "grade": 15},
]

sorted_students = sorted(students, key=lambda x: x["grade"], reverse=True)

for student in sorted_students:
    print(student["name"], student["grade"])