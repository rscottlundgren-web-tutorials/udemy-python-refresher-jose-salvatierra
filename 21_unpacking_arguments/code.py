def multiply(*args):
    # print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def add(x, y):
    return x + y


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


nums_1 = [3, 5]
nums_2 = {"x": 15, "y": 25}

print(multiply(1, 3, 5))
print(add(*nums_1))
print(add(**nums_2))        # print(add(x=nums_2["x"], y=nums_2["y"]))
print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="*"))
