# This is the helper function that subtracts 7 from the given number
def subtract_seven(num):
    return num - 7

# This is the main function that uses the helper
def main():
    # Ask the user for a number
    number = int(input("Enter a number to subtract from 7: "))

    # Call the helper function and store the result
    result = subtract_seven(number)

    # Print the result
    print(f"Result after subtracting is: {result}")

# Run the main function
main()
