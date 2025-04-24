#Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).
def main():
    print("Welcome to the Agreement Bot!")
    print("I will ask you a series of questions to determine if we can agree on something.")

    user_input = input("What is your favourite place to visit? ")
    print(f"That's interesting! I like to visit {user_input} too.")
    user_input = input("What is your favourite type of music? ")
    print(f"That's cool! I enjoy listening to {user_input} as well.")
    user_input = input("What is your favourite food? ")
    print(f"Yum! I love {user_input} too.")
    user_input = input("What is your favourite hobby? ")
    print(f"That's awesome! I also enjoy {user_input}.")
    user_input = input("What is your favourite pet animal? ")
    print(f"Great choice! I also like {user_input}.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()