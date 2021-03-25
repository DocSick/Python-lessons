requested_toping = 'mushrooms'

if requested_toping != 'anchovies':
    print("Hold the anchovies")


requested_toping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toping:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toping:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toping:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("\nFinished making your pizza!")


requested_toping = ['mushrooms', 'green peppers', 'extra cheese']

for requested_toping in requested_toping:
    if requested_toping == 'green peppers':
        print("Sorry, we are out of green pepprs right now.")
    else:
        print(f"Adding {requested_toping}.")

print("\nFinished making your pizza!")

requested_toping = []
if requested_toping:
    for requested_toping in requested_topings:
        print(f"Adding {requested_toping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']

requested_toping = ['mushrooms', 'french fries', 'extra cheese']

for requested_toping in requested_toping:
    if requested_toping in available_toppings:
        print(f"Adding {requested_toping}.")
    else:
        print(f"Sorry, we don't have {requested_toping}.")

print("\nFinished making your pizza!")