def main():
    
    import random

    die1 = random.randint(1, 6) # Random number between 1 and 6
    die2 = random.randint(1, 6) # Random number between 1 and 6

    print(f"Die 1: {die1}") # Print the value of die1
    print(f"Die 2: {die2}") # Print the value of die2
    print(f"Total: {die1 + die2}") # Print the total of die1 and die2


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()