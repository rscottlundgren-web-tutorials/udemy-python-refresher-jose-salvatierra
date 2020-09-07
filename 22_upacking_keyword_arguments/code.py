def named_1(**kwargs):
    print(kwargs)


def named_2(name, age):
    print(name, age)


def print_nicely(**kwargs):
    named_1(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


def both(*args, **kwargs):
    print(args)
    print(kwargs)


def myfunction(**kwargs):
    print(kwargs)


details = {"name": "Bob", "age": 25}

named_1(name="Bob", age=25)
named_2(**details)
print_nicely(name="Bob", age=25)
both(1, 3, 5, name="Bob", age=25)
# myfunction(**"Bob")                   # Error, must be mapping
# myfunction(**None)                    # Error
