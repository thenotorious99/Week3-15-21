class Book:
    def __init__(self, title, autor, year):
        self.title = title
        self.autor = autor
        self.year = year

book1 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki", 2001)

print("Title:", book1.title)
print("Autor:", book1.autor)
print("Year:", book1.year)


