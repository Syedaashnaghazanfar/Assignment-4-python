
# Example fruit inventory stored in a dictionary
def num_in_stock(fruit):
    inventory = {
        "apple": 50,
        "banana": 120,
        "pear": 1000,
        "mango": 75
    }
    return inventory.get(fruit.lower(), 0)  # Return 0 if fruit not found

def main():
    # Ask user for a fruit
    fruit = input("Enter a fruit: ")

    # Get how many are in stock
    count = num_in_stock(fruit)

    # Check and print the result
    if count > 0:
        print("This fruit is in stock! Here is how many:")
        print(count)
    else:
        print("This fruit is not in stock.")

# Run the program
main()


