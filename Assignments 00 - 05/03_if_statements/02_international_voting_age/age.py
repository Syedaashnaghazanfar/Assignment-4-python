# This program checks if a user is eligible to vote in three different countries based on their age.
def main():
    peturksbouipo :int = 16
    stanlau :int = 25
    mayengua :int = 48 

    user_age = int(input("Enter your age: "))

    if user_age>=peturksbouipo:
        print(f"You are {user_age} years old, you can vote in Peturksbouipo.Where voting age is {peturksbouipo} years old.")  
    else:
        print(f"You are {user_age} years old, you cannot vote in Peturksbouipo.Where voting age is {peturksbouipo} years old.")

    if user_age>=stanlau:
        print(f"You are {user_age} years old, you can vote in Stanlau.Wheree voting age is {stanlau} years old.")
    else:
        print(f"You are {user_age} years old, you cannot vote in Stanlau.Where voting age is {stanlau} years old.")

    if user_age>=mayengua:
        print(f"You are {user_age} years old, you can vote in Mayengua.Where voting age is {mayengua} years old.")
    else:
        print(f"You are {user_age} years old, you cannot vote in Mayengua.Where voting age is {mayengua} years old.")


if __name__ == "__main__":
    main()