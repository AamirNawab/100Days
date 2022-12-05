  """
  Program to calculate the tip should be paid based on bill
  output of program: give the total tip and bill for an individual to pay 
  
  """


bill = float(input("How much was the bill? "))
people = int(input("Total number of people to split the bill with? "))
percent = int(input("What percent of the bill would you like to tip? "))

split = bill / people
tip = split * (percent / 100)
total_bill = split + tip

print(f"The total tip is {tip}")
print(f"The total bill is {total_bill}")
