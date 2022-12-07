"""
A program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number.
"""



print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")




def true_count(name):
    count_true = name.count('t') + name.count('r') + name.count('u') + name.count('e')
    return count_true


def love_count(name):
    count_love = name.count('l') + name.count('o') + name.count('v') + name.count('e')
    return count_love


def count_true(name1, name2):
    first_name = name1.lower()
    second_name = name2.lower()
    count1 = true_count(first_name) + true_count(second_name)
    count2 = love_count(first_name) + love_count(second_name)
    return str(count1) + str(count2)

love_score = int(count_true(name1, name2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.") 
else:
    print(f"Your score is {love_score}." )