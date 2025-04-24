import sys

def madlibs():
    print("\nWelcome to Python MadLibs, let's tell a fun story.\n")

    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb_past = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    plural_noun = input("Enter a plural noun: ")
    verb_ing = input("Enter a verb ending in -ing: ")


    story = (
        f"Today I went to the zoo and saw a {adjective1} {noun1}. "
        f"It {verb_past} {adverb} through the {adjective2} forest. "
        f"Then, it found a {noun2} and started {verb_ing} with some {plural_noun}!"
    )


    print("\nHere's your MadLibs story:\n")
    print(story)

if __name__ == "__main__":

    madlibs()
  