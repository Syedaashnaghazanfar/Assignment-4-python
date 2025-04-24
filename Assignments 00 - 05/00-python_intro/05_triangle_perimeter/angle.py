#alculating triangle perimeter using sides

def main():
    side1 = int(input("Enter the lenght od side 1:"))
    side2 = int(input("Enter the lenght od side 2:"))
    side3 = int(input("Enter the lenght od side 3:"))
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is: ", perimeter)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()