# Цикл while в действии
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1


# Команда continue и продолжение цикла
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Предотвращение зацикливания
x = 1
while x <= 5:
    print(x)
    x += 1

# # Бесконечный цикл!
# x = 1
# while x <= 5:
# print(x)