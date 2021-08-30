#
# Jared Spector
# 08/22/2021
# This program converts a user-entered Celsius temperature and
# converts it to Fahrenheit


# Get the Celsius temperature.
celsius = input('Enter Celsius temperature:')
celsius = int(celsius)

# Calculate the Fahrenheit equivalent.
fahrenheit = (9.0 / 5.0) * celsius + 32
format_fahrenheit = "{:.2f}".format(fahrenheit)

# Display the Fahrenheit temperature.
print(f"That is equal to {format_fahrenheit} degrees Fahrenheit")
