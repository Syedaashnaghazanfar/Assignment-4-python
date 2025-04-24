def print_multiple(message, repeats):
    # Loop through the number of times specified
    for _ in range(repeats):
        print(message)

def main():
    # Ask user to type a message
    message = input("Please type a message: ")

    # Ask user how many times to repeat that message
    repeats = int(input("Enter a number of times to repeat your message: "))

    # Call the function to print the message multiple times
    print_multiple(message, repeats)

# Run the main function
main()
