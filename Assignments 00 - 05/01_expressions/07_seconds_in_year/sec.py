def main():
    seconds_in_year: int = 31536000

    years:int = int(input("Enter the number of years: "))

    total_seconds: int = years * seconds_in_year

    print(f"{years} years is equal to {total_seconds} seconds!")
if __name__ == '__main__':
    main()