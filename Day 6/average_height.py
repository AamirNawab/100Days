"""
A program that calculates the average student height from a List of heights.
"""



student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0
for x in student_heights:
  total += x

items = 0

for x in student_heights:
  items += 1

print(round(total / items)) 
