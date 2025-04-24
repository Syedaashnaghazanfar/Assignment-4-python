#dice simulator showing variable scope importance 

import random

num_dice = 6

def roll_dice():
    dice1 = random.randint(1, num_dice)
    dice2 = random.randint(1, num_dice)
    dice3 = random.randint(1, num_dice)
    print(f"Total of the dice is{dice1 + dice2 + dice3}")

def main():
    dice1 : int = 10
    print(f"the value of dice1 is {dice1}") #this shows that we cannot access the dice1 variable in the roll_dice function
    #rolling die three time 
    roll_dice()
    roll_dice() 
    roll_dice()
    print(f"the value of dice1 is {dice1}") #even after using funtion the value of dice1 is not changed

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()