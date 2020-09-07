default_y = 3


def add(x, y=8):
    print(x + y)


def default_add(x, y=default_y):
    sum = x + y
    print(sum)


add(5)
default_add(2)

default_y = 5

default_add(2)
