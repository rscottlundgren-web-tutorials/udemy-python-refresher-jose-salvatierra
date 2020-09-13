class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # User-Focused
    # Goal of this method is to print out a nice easy-to-read string for users
    # Called when you want to turn your object into a string
    def __str__(self):
        return f"Person {self.name}, {self.age} years old."

    # Developer Focused
    # Goal is to return a string that allows us to recreate the original object easily
    # Called when you want to print out an unambiguous representation of an object so you can recreate the object
    def __repr__(self):
        return f"<Person('{self.name}', {self.age})>"


bob = Person("Bob", 35)

print(bob)
print(bob.__repr__())
