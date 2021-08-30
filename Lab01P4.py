# Jared Spector
# 08/22/2021
# This is a program to calculate a customer total at a  used bookstore

#Constants
pap = 2.5
mag = 3.95
har = 7.0
tax = 0.07

#User inputs
papNum = input("Enter the number of paperback books:")

harNum = input("Enter the number of hardback books:")
harNum = int(harNum)
magNum = input("Enter the number of magazines:")
magNum = int(magNum)

#Calculation
sub = (papNum*pap) + (harNum*har) + (mag*magNum)
subtotal = "{:.2f}".format(sub)
taxTot = sub * tax
taxTotal = "{:.2f}".format(taxTot)
Tot = sub + taxTot
Total = "{:.2f}".format(Tot)

#Outputs
print("Subtotal: $" + subtotal)
print("Tax: $" + taxTotal)
print("Your total is: $" + Total)
