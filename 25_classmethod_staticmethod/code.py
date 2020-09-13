class ClassTest:
    # Used for most things
    # Used often
    # When you want to produce an action that uses the data inside the object that you created
    # When you want to call a method to modify data inside self
    def instance_method(self):
        print(f"Called instance_method of {self}")

    # Used as factories
    # Used often
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    # Used to place a method inside a class
    # Used rarely
    @staticmethod
    def static_method():
        print("Called static_method")


test = ClassTest()
test.instance_method()

ClassTest.class_method()

ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)


book = Book("Harry Potter", "hardcover", 1500)
neal_stephenson = Book.hardcover("REAMDE", 1600)
neil_gaiman = Book.paperback("American Gods", 750)


print(Book.TYPES)
print(book)
print(book.name)
print(neal_stephenson)
print(neil_gaiman)
