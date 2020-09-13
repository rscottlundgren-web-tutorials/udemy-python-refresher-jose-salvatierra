class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


neal_stephenson = Book("REAMDE")
neil_gaiman = Book("Neverwhere")
library = BookShelf(neal_stephenson, neil_gaiman)

print(library)
