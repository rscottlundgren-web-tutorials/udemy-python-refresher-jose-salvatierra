# name = input("Enter your name: ")
# print(name)


size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8
print(f"{square_feet} sq/ft is equal to {square_metres:.2f} sq/metres.")
