import random 
# Simple random password generator
print("Now let's generate a random password!")
    # Ask user for password length
try:
        length = int(input("Enter desired password length (e.g., 8): "))
except ValueError:
        print("Invalid input. Using default length of 8.")
        length = 8

    # Define character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
symbols = '!@#$%^&*()'
all_chars = letters + digits + symbols

    # Generate password
password = ''.join(random.choice(all_chars) for _ in range(length))
print(f"Your random password is: {password}")
