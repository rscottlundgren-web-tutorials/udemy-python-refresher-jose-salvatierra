user_age = int(input("Enter your age: "))
leap_years = int(user_age / 4)
days = int(leap_years * 366) + int((user_age - leap_years) * 365)
seconds = days * 86400
print(f"Your age, {user_age}, is equal to {seconds} seconds.")
