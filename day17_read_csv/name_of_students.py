import csv

with open("students.csv") as f:
    read = csv.reader(f)
    next(read)

    for row in read:
        names = str(row[0])

        if names.startswith("A"):
            print(names)