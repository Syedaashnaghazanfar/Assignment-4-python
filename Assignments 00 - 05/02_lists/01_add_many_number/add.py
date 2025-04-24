def add_many_numbers(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    return total_sum

def main():
    numbers = [1,2,3,4,5]
    total = add_many_numbers(numbers)
    print(total)

if __name__ == '__main__':
    main()



    