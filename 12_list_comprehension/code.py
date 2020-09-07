numbers = [1, 3, 5]
doubled = [num * 2 for num in numbers]

# for num in numbers:
#     doubled.append(num * 2)

print(doubled)


friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends is:", id(friends), "starts_s is:", id(starts_s))
