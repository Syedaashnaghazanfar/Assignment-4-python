
def add_to_list(my_list,data):
    my_list.append(data)

def main():
  my_list = []
  print(f"The list before is {my_list}") #or convert this into the str for adding plus icon
  item_in_list = input("Enter an item to add to the list: ")
  add_to_list(my_list,item_in_list)
  print(f"The list after is {my_list}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()