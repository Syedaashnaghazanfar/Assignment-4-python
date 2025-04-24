def main():
    def count_even(lst=None):
    # If no list is provided, start collecting user input
        if lst is None:
            lst = []  # Create an empty list to store user inputs

        while True:
            # Prompt the user for an integer or press enter to stop
            user_input = input("Enter an integer or press enter to stop: ")
            
            # If input is empty, stop the loop
            if user_input == "":
                break

            try:
                # Try to convert input to integer and add to list
                number = int(user_input)
                lst.append(number)
            except ValueError:
                # If input is not a valid integer, show a message and continue
                print("Please enter a valid integer.")

    # Count the even numbers in the list
        even_count = 0
        for num in lst:
            if num % 2 == 0:
                even_count += 1  # Increment count if number is even

    # Print the result
        print(f"Number of even numbers: {even_count}")

if __name__ == "__main__":
    main()
# This code is a simple program that counts the number of even integers entered by the user. The user can enter integers one by one, and when they press enter without entering a number, the program will stop and display the count of even numbers.