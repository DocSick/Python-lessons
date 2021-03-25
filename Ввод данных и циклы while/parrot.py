# Как работает функция input()
massage = input("Tell me something, and I will repeat it back to you: ")
print(massage)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name}!")


# Пользователь решает прервать работу программы
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
massage = ""
while massage != 'quit':
    massage = input(prompt)

    if massage != 'quit':
        print(massage)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    massage = input(prompt)

    if massage == 'quit':
        active = False
    else:
        print(massage)