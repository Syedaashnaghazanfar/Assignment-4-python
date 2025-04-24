def add_into_list(my_list, val):
    my_list.append(val)
    print(f"The items in the list are: {my_list}")

def main():
    my_list = []
    
    while True:
        value = input("Enter a value to add to the list (or press Enter to stop): ")
        if value == "":
            break
        add_into_list(my_list, value)

if __name__ == '__main__':
    main()
