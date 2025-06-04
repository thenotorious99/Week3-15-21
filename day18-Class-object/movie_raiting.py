class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

    def high_raiting(self):
        return self.rating > 8

movies = [
    Movie("Inception", "Christopher Nolan", 8.8),
    Movie("The Room", "Tommy Wiseau", 3.7),
    Movie("Interstellar", "Christopher Nolan", 8.6),
    Movie("Avatar", "James Cameron", 7.8),
    Movie("The Godfather", "Francis Ford Coppola", 9.2)
]

print("Movies with rating up 8:")
for movie in movies:
    if movie.high_raiting():
        print(f"- {movie.title} ({movie.rating})")