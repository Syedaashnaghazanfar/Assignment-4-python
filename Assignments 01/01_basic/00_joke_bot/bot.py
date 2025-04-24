import random 


PROMPT = "What do you want? "
SORRY = "Sorry I only tell jokes"

# List of jokes in an array 
JOKES = [
    "Here is a joke for you! Sophia goes to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. She returns with 13 liters of milk.",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
    "Why did the function break up with the loop? Because it had too many issues to resolve.",
    "I told my computer I needed a break, and now it won’t stop sending me vacation ads.",
    "Debugging: Being the detective in a crime movie where you are also the murderer."
]

def main():

    user_input = input(PROMPT)

    
    if user_input == "Joke".lower():
        joke = random.choice(JOKES)  # Pick a random joke from the array 
        print(joke)
    else:
        print(SORRY)

# Run the program
main()

#this bot gives some random joke to a user when he promts joke