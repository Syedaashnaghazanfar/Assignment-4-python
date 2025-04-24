def main():
    # This program is a Mad Libs game that asks the user for various words and then generates a story using those words.
    # The user is prompted to enter a noun, verb, adjective, and adverb, which are then used to create a story.
    
    noun = str(input("Enter a noun: "))
    verb = str(input("Enter a verb: "))
    adjective = str(input("Enter an adjective: "))
    adverb = str(input("Enter an adverb: "))

    # The story is then printed using the words provided by the user.
    print(f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}.")
    print(f"One day, the {noun} decided to go on an adventure and {verb} all the way to the {adjective} mountain.")
    print(f"Along the way, the {noun} met a {adjective} friend who also loved to {verb} {adverb}.")
    print(f"Together, they had the most {adjective} time {verb}ing and {adverb} exploring the world around them.")
    print(f"And they lived happily ever after, always {verb}ing {adverb} together.")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()