inches_in_foot :int = 12

def main():
    foot = int(input("Enter the number of feet: "))
    inches = foot * inches_in_foot
    print(f"{foot} feet is equal to {inches} inches.")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
