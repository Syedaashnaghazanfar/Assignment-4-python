#age calculator for some kids

def main():

    anton = 20
    beth = anton + 6 #6 yrs older then anton
    chen = beth + 20 #chen id 20 yrs older then beth
    drew = chen + anton  #drew is chen plus antons age
    ethan = chen #same as ches age

    print(f"Anton is {anton} years old.")
    print(f"Beth is {beth} years old.")
    print(f"Chen is {chen} years old.")
    print(f"Drew is {drew} years old.")
    print(f"Ethan is {ethan} years old.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()