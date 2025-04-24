def get_last_item(last):
    print(f"The last item in the list is {last[-1]}")

def main():
    list1 = [ "hello", "world", 1, 2, 3]
    print(f"The full list before is {list1}")
    get_last_item(list1)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()