import csv

with open("grades.csv") as file:
    grades = csv.reader(file, delimiter=';')
    next(grades) # preskachame zaglavniq red
    for row in grades:
        name = row[0]
        grade = float(row[1])
        if grade <= 4.50:
            print(name)
