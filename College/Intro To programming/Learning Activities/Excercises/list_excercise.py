# Create a list with two sublists.
my_list = [1, 2, 3], ["a", "b", "c"]

# Append 4 to the first sublist and print it.
my_list[0].append(4)
print(my_list[0])

# Remove the last element from the first sublist and print it.
my_list[0].pop()
print(my_list[0])

# Append "d" to the second sublist and print it.
my_list[1].append("d")
print(my_list[1])

# Remove the last element from the second sublist and print it.
my_list[1].pop()
print(my_list[1])

# Create a nested list.
listception = [[1, 2, 3], [4, 5, 6]], [['a', 'b', 'c'], ['d', 'e', 'f']]

# Print specific elements from the nested list.
print(listception[0][1][2])  # Print '6'
print(listception[1][0][1])  # Print 'b'

# Remove the first element (4) from the inner list within the first sublist and print it.
listception[0][1].pop(0)
print(listception[0][1])  # Print [5, 6]
