a = []
# b = a
b = []
c = 8597
d = 8597

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b))

print(id(c))
print(id(d))

c = 8598

print(id(c))
print(id(d))
