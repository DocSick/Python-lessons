pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Позиционные аргументы
def descride_pet (pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# descride_pet('hamster', 'harry')
# descride_pet('dog', 'willie')
# descride_pet(pet_name='harry')
# descride_pet(pet_name='harry', animal_type='hamster')
descride_pet('willie')
descride_pet(pet_name='willie')

descride_pet('harry', 'hamster')
descride_pet(pet_name='harry', animal_type='hamster')
descride_pet(animal_type='hamster', pet_name='harry')