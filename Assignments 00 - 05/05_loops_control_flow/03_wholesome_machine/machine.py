
AFFIRMATION = "I am capable of doing anything I put my mind to."
def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_input = input()

    while  user_input != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input()
    print("Congratulations! You typed the affirmation correctly.")

# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    main()