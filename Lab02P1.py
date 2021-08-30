#
# Jared Spector
# 8/29/2021
# Programming Exercise 3-3: Age Classifier
#

# Get the person's age.
age = int(input('Enter age: '))

# Determine if the person is an infant, child,
# teenager, or adult, and display the result.
if age < 1:
    print('Infant')
elif age <= 13:
    print('Child')
elif age <= 19:
    print('Teenager')
elif age >=20:
    print('Adult')
