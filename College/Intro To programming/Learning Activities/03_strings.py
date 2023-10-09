# Indexing
word = "Hello World!"
print(word[1])    # Print the character at index 1 ('e')
print(word[-1])   # Print the last character ('!')

# Slicing
print(word[6:])       # Print from index 6 to the end ('World!')
print(word[6:11])     # Print from index 6 to 10 ('World')
print(word[6:11:2])   # Print from index 6 to 10, skipping every other letter ('Wrd')

# Reversing string
print(word[::-1])     # Reverse and print the string ('!dlroW olleH')

# Extracting a substring from lorem_ipsum
lorem_ipsum = "..."  # (Large text, omitted for brevity)
print(lorem_ipsum[len(lorem_ipsum) - 12:len(lorem_ipsum):1])

# Extracting a substring from word_2
word_2 = "Hello whatsup good day"
print(word_2[len(word_2) - 8:len(word_2):1])

# Upper, Lower, and Capitalize
print("Upper, Lower, and Capitalize")
name_1 = "Corey Ford"
print(name_1.upper())               # Uppercase the string
print(name_1.lower())               # Lowercase the string
print(name_1.lower().capitalize())  # Lowercase and then capitalize the string

# Splitting
print("Splitting:")
name_split = name_1.split(" ")      # Split the string into a list based on spaces
print(name_split)
print(name_split[0])                # Print the first element of the list
print(name_split[0][0])             # Print the first character of the first element
print(name_split[0].lower(), name_split[1].lower())  # Print both names in lowercase

# .format method
first_name = "Corey"
last_name = "Ford"
full_name = "{1} {0}".format(first_name, last_name)  # Format and concatenate strings
print(full_name)  # Print the formatted full name ('Ford Corey')
