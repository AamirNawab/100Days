"""
A program thats randomly generates password

"""


import random

# User input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Lists for characters for password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# random choice on each list depending on user input
choose_letter = random.choices(letters, k=nr_letters)
choose_symbols = random.choices(symbols, k=nr_symbols)
choose_numbers = random.choices(numbers, k=nr_numbers)


# append random pick to list
random_list = []
for i in choose_letter:
  slists = i
  random_list.append(slists)
for i in choose_symbols:
  slists = i
  random_list.append(slists)
for i in choose_numbers:
  slists = i
  random_list.append(slists)

#shuffle list to randomise sequence
random.shuffle(random_list)

# print each list element as one string. 
mystring = ''
for i in random_list:
  mystring += i

print(mystring)



  
