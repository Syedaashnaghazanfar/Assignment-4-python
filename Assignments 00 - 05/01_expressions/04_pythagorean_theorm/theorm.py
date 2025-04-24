import math 

def main():
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)  # bc = sqrt(ab^2 + ac^2)
    print("The length of BC (the hypotenuse) is: " + str(bc)) # This is the length of the hypotenuse


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()