"""
a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

output should be the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.

"""
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

message = f"Your bmi is {bmi}, you are "

if bmi < 18.5:
    print(message, "underweight")
elif bmi >= 18.5 and bmi < 25:
    print(message, 'normal weight')
elif bmi >= 25 and bmi < 30:
    print(message, 'slighty overweight')
elif bmi  >=30 and bmi < 35:
    print(message, 'obese')
else:
    print(message, 'clinically obese')
    
