required_height : int = 50 # arbitrary units :)

def main():
    height = float(input("WHAT IS YOUR HEIGHT? "))
    if height >= required_height :
        print("You can ride the rollercoaster!")
    else:
        print("You're not tall enough to ride the rollercoaster, but maybe next year!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()