import random

num_characters = input("How many characters do you want your password to be?")
print("Your password is: ", end = "")
for i in range(int(num_characters)):
    if i == num_characters:
        print(chr(random.randint(33,126)))
    else:
        print(chr(random.randint(33,126)), end = "")