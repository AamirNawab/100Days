"""
Create a program that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.

"""
age = input("What is your current age? ")

days = (90 * 365) - 365 * int(age) 
weeks =  (90 * 52)- 52 * int(age)
months = (90 * 12) - 12 * int(age)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
