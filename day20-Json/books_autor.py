import json

books = [
    {"title": "Cant Hurt Me", "autor": "David Goggins", "year": 2018},
    {"title": "Never Finished", "autor": "David Goggins", "year": 2022},
    {"title": "Green Apple", "autor": "Jony Hood", "year": 2009},
    {"title": "Short Money", "autor": "John Brook", "year": 2008},
]

with open("books.json", "w") as f:
    json.dump(books, f)

with open("books.json", "r") as f:
    book = json.load(f)

for row in book:
    if row["year"] > 2010:
        print(f"Title: {row['title']} - Year: {row['year']}")
