def add(x, y):
    # print(x + y)
    return x + y


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool! A divisor may not be 0!"


add(5, 8)
result_add = add(5, 8)
result_div1 = divide(15, 3)
result_div2 = divide(15, 0)
print(result_add)
print(result_div1)
print(result_div2)
