# Копирование списка
my_foods = ['pizza', 'falafel', 'carrot', 'cake']
friend_foods = my_foods[:]

# Не работает:
# friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print(f"\nThe irst three items in the list are:{my_foods [:3]}")
print(f"\nThree items from te middle of the list are:{my_foods [1:4]}")
print(f"\nThe last three items in the list are: {my_foods [-3d:]}")


