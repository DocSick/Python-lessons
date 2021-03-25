import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
filename = 'username.json'
try:
    with open(filename) as f:
        username = input("What is your name? ")
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you come back, {username}!")
else:
    print(f"Welcome back {username}!")




import json

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
     """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
    print(f"Welcome back, {username}!")
else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
greet_user()