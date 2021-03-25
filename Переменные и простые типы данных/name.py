# Преобразовывает первый символ кажлого слова в строке к верхнему регистру
name = "ada lovelace"
print(name.title())

# Верхний и нижний регист
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Объединение
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# Объединение и каждая первая буква в слове выводится в верхнем регистре
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Всё вместе
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)