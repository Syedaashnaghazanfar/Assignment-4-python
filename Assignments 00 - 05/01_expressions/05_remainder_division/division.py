def main():
    divident :int = int(input("Enter the dividend: "))
    divisor :int = int(input("Enter the divisor: "))

    quotient :int = divident // divisor #integer division
    remainder :int = divident % divisor #modulus operator

    print(f"The quotient is {quotient} and the remainder is {remainder}.")
    # The quotient is the result of the integer division
    # The remainder is the result of the modulus operator


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()