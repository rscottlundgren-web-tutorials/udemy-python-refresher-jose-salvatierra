def divide(dividend, divisor):
    if divisor == 0:
        # print("Divisor cannot be 0.")
        # return
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


# divide(15. 0)

# grades = []
grades = [78, 99, 85, 100]

print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")

students = [
    {"name": "Bob", "grades": [75, 90]},
    # {"name": "Rolf", "grades": []},
    {"name": "Rolf", "grades": [100, 70]},
    {"name": "Jen", "grades": [100, 90]},
]

print('-------')
print("Welcome to the average grade program.")
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
