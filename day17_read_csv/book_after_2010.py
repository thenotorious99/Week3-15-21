import csv

with open("books.csv") as f:
    read = csv.reader(f)
    next(read)
    
    for row in read:
        name = row[0]
        autor = row[1]
        year = int(row[2])

        if year > 2010:
            print(name)