# Кортеж
dimension = (200, 50)
print(dimension[0])
print(dimension[1])

# Нельзя изменить кортеж
# dimension = (200, 50)
# dimension[0] = 250

for dimension in dimension:
    print(dimension)

print("Original dimension:")
for dimension in dimension:
    print(dimension)


dimension = (400, 100)
print("\nModified dimensions:")
for dimension in dimension:
    print(dimension)

test = (1, 2, 3, 4, 5)
for test in test:
    print(test)
