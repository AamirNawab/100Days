"""
A rock paper scissors program

"""




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
list = [rock, paper, scissors]


print("Hi User, Welcome to Rock, Paper, Scissors")
pick = input("Pick 0 for Rock, 1 for Paper, 2 for scissors: ")

computer =  random.randint(0,2)
pick = int(pick)

print("You have picked:")
print(list[pick])

print("Computer has picked: ")
print(list[computer])



if pick == 0 and computer == 1:
    print("You lose")
elif pick == 1 and computer == 2:
    print("You lose")
elif pick == 2 and computer == 0:
    print("You lose")
elif pick == computer:
    print("Draw!")
else:
    print("You won!")

