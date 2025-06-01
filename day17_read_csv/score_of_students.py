import csv

count = 0

with open("scores.csv") as f:
    read_score = csv.reader(f)
    next(read_score)

    for row in read_score:
        names = row[0]
        score = int(row[1])

        if score > 90:
            count += 1
print(f"People with score more big 90: {count}")
