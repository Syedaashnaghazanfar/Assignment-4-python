# Fahrenheit to Celsius conversion
# Formula: (F - 32) * 5/9 = C
degrees_fahrenheit = int(input("Enter temperature in Fahrenheit: "))
degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

print(f"{degrees_fahrenheit} is equal to {degrees_celsius} in celsius")