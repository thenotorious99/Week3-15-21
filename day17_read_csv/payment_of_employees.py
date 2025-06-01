import csv

with open("employees.csv") as f:
    paycheck = csv.reader(f)
    next(paycheck)

    for row in paycheck:
       name = row[0]
       money = int(row[1])

       if money >= 3000:
           print(name)
