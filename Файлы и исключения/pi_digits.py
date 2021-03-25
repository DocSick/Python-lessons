filename = '/home/doc/Документы/Python/Txt/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line

brirthday = input("Enter your birthday, in the form mmddyy:")
if brirthday in pi_string:
    print("Your birthday appers in the first million digits of pi@")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print(pi_string)
print(len(pi_string))