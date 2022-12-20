"""
A program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
"""

number = 0
for x in range(0,101,2):
    number += x

print(number)
