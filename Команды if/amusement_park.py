# Использования if elif else
age = 12

if age < 4:
    print("You admission cost is $0.")
elif age < 18:
    print("You admission cost is $25.")
else:
    print("You admission cost is $40.")

# Упрощенный код
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

# Блоков elis может быть сколько угодно
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

# Функция необязательно должна заканчиваться на else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")
