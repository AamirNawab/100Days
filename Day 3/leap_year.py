"""
 A program that works out whether if a given year is a leap year.
This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400

"""
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print("leap year")
else:
    print("Not leap year.")
