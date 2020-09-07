def add(x, y):
    result = x + y
    print(result)


def say_hello():
    print("Hello!")


def hello(name, surname):
    print(f"Hello, {name} {surname}!")


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("You fool! A divisor cannot be zero!")


add(5, 3)
say_hello()
hello("Bob", "Smith")
hello(surname="Bob", name="Smith")
divide(3, 5)
divide(3, 0)
