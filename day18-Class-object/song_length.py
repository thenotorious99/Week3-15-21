class Song:
    def __init__(self, title, length_in_min):
        self.title = title
        self.length_in_min = int(length_in_min)

    def length_song(self):

        if self.length_in_min > 4:
          return f"This song is long(over 4 minutes): {self.title}, {self.length_in_min}"
        else:
            return f"This song is short: {self.title}, {self.length_in_min}"

music = Song("Ibiza summer mix", 5)

print(music.length_song())

