# this program give the double of the items in the list 
def main():
    numbers: list[int] = [1, 2, 3, 4]

    for i in range(len(numbers)):  
        elem_at_index = numbers[i]  
        numbers[i] = elem_at_index * 2  

    print(numbers)  


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()