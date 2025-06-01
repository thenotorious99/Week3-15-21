import csv

with open("products.csv") as f:
    product = csv.reader(f)
    next(product)

    for row in product:
        name = row[0]
        quality = int(row[1])

        if quality < 10:
            print(name)