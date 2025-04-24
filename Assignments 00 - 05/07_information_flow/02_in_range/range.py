def in_range(n, low, high):
    # Returns True if n is between low and high, inclusive
    return low <= n <= high

def main():
    # Ask user for the number they want to check
    n = int(input("Enter a number to check: "))
    
    # Ask for the low and high bounds of the range
    low = int(input("Enter the low end of the range: "))
    high = int(input("Enter the high end of the range: "))

    # Call the function and print the result
    if in_range(n, low, high):
        print(f"{n} is within the range [{low}, {high}].")
    else:
        print(f"{n} is NOT within the range [{low}, {high}].")

# Run the program
main()
