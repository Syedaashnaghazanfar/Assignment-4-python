import random  # Import the random library

def main():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(10):  # We need to repeat the process 10 times
        print(random.randint(1, 100), end=" ")  # Generate a random number and print it on the same line

# Run the program
main()
