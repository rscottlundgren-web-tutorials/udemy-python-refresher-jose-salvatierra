def add(x, y):
    return x + y


def double(x):
    return x * 2


sequence = [1, 3, 5, 7, 9]
doubled = [double(x) for x in sequence]
doubled_alt_1 = list(map(double, sequence))
doubled_alt_2 = list(map(lambda x: x * 2, sequence))

print(add(5, 7))
print((lambda x, y: x + y)(5, 7))
print(doubled)
print(doubled_alt_1)
print(doubled_alt_2)
