from car import ElectricCar

my_testa = ElectricCar('tesla', 'model', 2019)

print(my_testa.get_descriptive_name())
my_testa.battery.describe_battery()
my_testa.battery.get_range()