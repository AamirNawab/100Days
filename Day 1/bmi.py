"""
This a simple program that calculates BMI to demonstrate python's print(), user input, data types and operators

"""


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
print(round(bmi))
