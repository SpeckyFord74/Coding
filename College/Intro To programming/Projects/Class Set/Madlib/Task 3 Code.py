# Import the random module to use for random value selection
import random

# Define a function named mad_lib_gen
def mad_lib_gen():
    # Initialize empty dictionaries to store user-entered nouns and adjectives
    user_noun = {}
    user_adj = {}

    # Define tuples containing nouns and adjectives to be used later in the story
    nouns = ("noun1", "noun2", "noun3", "noun4", "noun5", "noun6")
    adjectives = ("adj1", "adj2", "adj3", "adj4")

    # Loop to collect user input for nouns and store them in the user_noun dictionary
    for noun in nouns:
        user_noun[noun] = input("Please enter a noun: ")
    # Print the first entered noun (for demonstration purposes)
    print(user_noun["noun1"])

    # Loop to collect user input for adjectives and store them in the user_adj dictionary
    for adjective in adjectives:
        user_adj[adjective] = input("Please enter an adjective: ")
    # Print the first entered adjective (for demonstration purposes)
    print(user_adj["adj1"])

    # Collect additional user inputs for various story elements
    name = input("Enter a name: ")
    colour = input("Enter a colour: ")
    verb = input("Enter a verb: ")
    ed_verb = input("Enter a verb ending with -ed: ")
    adverb = input("Enter an adverb: ")
    num = int(input("Enter a whole number: "))

    # Construct and print the Mad Libs story using the collected inputs and random selections
    print(f"Title: The Mysterious {random.choice(list(user_noun.values()))}\nOnce upon a time in an {random.choice(list(user_adj.values()))} land, a {random.choice(list(user_noun.values()))} disappeared.\n {name}, the {random.choice(list(user_adj.values()))} {random.choice(list(user_noun.values()))}, {adverb} {verb} to find it.\n After {num} {random.choice(list(user_adj.values()))} days, they discovered a {random.choice(list(user_noun.values()))} next to a {colour} {random.choice(list(user_noun.values()))}. They {ed_verb} the {random.choice(list(user_noun.values()))} and celebrated with a {random.choice(list(user_adj.values()))} feast. The end.")

# Call the mad_lib_gen function to generate and display the Mad Libs story
mad_lib_gen()
 