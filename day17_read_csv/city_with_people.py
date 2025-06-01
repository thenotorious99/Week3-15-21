import csv

with open("cities.csv") as f:
    people = csv.reader(f)
    next(people)

    for row in people:
        names_of_cities = row[0]
        citisen = int(row[1])

        if citisen > 1000000:
            print(f"Names of cities: {names_of_cities}")