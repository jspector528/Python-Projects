#
# Jared Spector
# 08/22/2021
# This program converts a user-entered Fahrenheit temperature and
# converts it to Celsius


# Get the Fahrenheit temperature.
fahrenheit = input('Enter Fahrenheit temperature:')
fahrenheit = int(fahrenheit)

# Calculate the Celsius equivalent.
celsius = (5/9) * (fahrenheit - 32)
format_celsius = "{:.2f}".format(celsius)

# Display the Celsius temperature.
print(f"That is equal to {format_celsius} degrees Celsius")
