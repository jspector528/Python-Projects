#
# Jared Spector
# 08/29/2021
# Simple Roulette Wheel Colors
#

# Get the pocket number from the user.
pocketNum = int(input('Enter a pocket number from 0 to 28: '))

# Determine if the pocket number is valid.
if pocketNum < 0 or pocketNum > 28:
    outputStr = 'Error: Invalid input'

# Determine the color of the pocket number.
else:
    # For pockets 1 through 10, the odd-numbered pockets
    # are red and the even-numbered pockets are black.
    if pocketNum >= 1 and pocketNum <= 10:
        if (pocketNum % 2) == 0:
            outputStr = 'Black'  # Even
        else:
            outputStr = 'Red'    # Odd

    # For pockets 19 through 28, the odd-numbered pockets
    # are red and the even-numbered pockets are black.
    elif pocketNum >= 19 and pocketNum <= 28:
        if (pocketNum % 2) == 0:
            outputStr = 'Black'  # Even
        else:
            outputStr = 'Red'    # Odd
    else:
        outputStr = 'Green'      # Zero

print(f'For pocket {pocketNum}, the color is {outputStr}')
