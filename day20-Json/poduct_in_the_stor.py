import json


products = [
    {"name": "Notebook", "price": 2, "Available": True},
    {"name": "Book", "price": 4, "Available": False},
    {"name": "Paper", "price": 5, "Available": True},
    {"name": "Python-Book", "price": 7, "Available": False},

]

with open("products.json", "w") as f:
    json.dump(products, f)

with open("products.json") as f:
    data = json.load(f)

for row in data:
    if row["Available"] == True:
        print(f"{row['name']} - Price: {row['price']}")