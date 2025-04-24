def main():
    # Ask the user to input a number
    curr_value = int(input("Enter a number: "))

    # Keep doubling the number while it is less than 100
    while curr_value < 100:
        # Double the current value
        curr_value = curr_value * 2
        
        # Print the current value after doubling
        print(curr_value, end=" ")

# Run the program
main()
