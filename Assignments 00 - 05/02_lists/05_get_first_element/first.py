def get_first_item(my_list):
    print(f"The first item in the list is {my_list[0]}")


def main():
    list1 = [1,2,3]
    print(f"The full list before is {list1}") 
    get_first_item(list1)
    

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()