
def phonebook():
    phonebook = {}

    while True:
        name = input("Enter you name:")
        if name == "":
            break
        number = input("Enter your number:")
        if number == "":
            break
        phonebook[name] = number


def print_book(phonebook):
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def look_for_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = phonebook()
    print_book(phonebook)
    look_for_numbers(phonebook)
