import json

movies = [
    {"name": "Sam v mraka", "genre": "Action", "Rating": 5},
    {"name": "Transporter", "genre": "Action", "Rating": 6},
    {"name": "Taxi 2", "genre": "Comedy", "Rating": 3},
    {"name": "365", "genre": "Love", "Rating": 6},
    {"name": "50 Cent", "genre": "Action", "Rating": 5}
]

with open("movies.json", "w") as f:
    json.dump(movies, f)

with open("movies.json", "r") as f:
    data = json.load(f)

for movie in data:
    if movie['genre'] == "Action":
        print(movie['name'])