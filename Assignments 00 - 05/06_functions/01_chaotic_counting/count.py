import random

# This is the global likelihood that done() returns True
DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i)

def main():
    chaotic_counting()
    print("I'm done.")

# Run the main function

if __name__ == "__main__":
    main()
# This code is a simple counting program that counts from 1 to 10, but it has a chance of stopping early based on a random condition.