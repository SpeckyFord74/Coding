# Create two lists.
list_1 = ["Apple", "Bannana", "Orange"]
list_2 = ["Pear", "Grapes", "Tomatoes"]

# Combine the two lists.
list_1.extend(list_2)

# Change the third-to-last element to "Plums".
list_1[-3] = "Plums"

# Remove the last element.
list_1.pop(-1)

# Print "Green" and "Apple" from the modified list.
print(list_1[1], list_1[0])
