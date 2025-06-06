class Game:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def adventure_rating(self):
        return self.genre == "Adventure"

games = [
    Game("Super Mario", "Adventure", 10),
    Game("Minecraft", "Adventure", 8),
    Game("GTA 5", "Animation", 10),
    Game("FIFA", "Adventure", 10)
]

print("Adventures games:")
for game in games:
    if game.adventure_rating():
        print(f" - {game.title}, {game.genre}")
