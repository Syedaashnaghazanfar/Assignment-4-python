def print_ones_digit(num):
    ones_digit = num % 10 
    print(f"The ones digit is {ones_digit}")

def main():
    # Ask the user to enter a number
    user_input = int(input("Enter a number: "))
    
    # Call the function with the user's number
    print_ones_digit(user_input)

# Run the main function
main()
