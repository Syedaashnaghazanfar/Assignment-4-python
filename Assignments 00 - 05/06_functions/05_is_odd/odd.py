#takes an input from the user and checks if the number is odd or even. If the number is even, it prints "even" and if the number is odd, it prints "odd". It does this for all numbers from 0 to the input number - 1.
def check(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

num = int(input("Enter a number: "))
for i in range(num):
    check(i)