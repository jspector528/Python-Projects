#
# Jared Spector
# 08/29/2021
# Bargain Used Books


subtotal = int(input("Enter total due: "))
loyal: str = input('Is Customer a member of loyalty program: (Y/N)')

if subtotal >= 75:
    subtotal = (subtotal * .9);
elif loyal == 'Y' or loyal == 'yes' and total <= 75:
    subtotal = (subtotal * .8); print('Thank you for being a loyal customer!')
elif loyal == 'Y' or loyal == 'yes' and total > 75:
    subtotal = (subtotal * .7); print('Thank you for being a loyal customer!')

tax = (subtotal * .7)
total = (subtotal + tax)
print('Subtotal:', format(subtotal, ".2f"))
print('Tax',format(tax, ".2f"))
print('Your total is: ', format(total, ".2f"))

