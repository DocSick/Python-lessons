# Словарь с однотипными объектами
favorite_languages = {'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name in favorite_languages.keys():
	print(name.title())


# Перебор всех ключей в словаре
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")


favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll")


# Перебор ключей словаря в определенном порядке
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")


# Перебор всех значений в словаре
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())