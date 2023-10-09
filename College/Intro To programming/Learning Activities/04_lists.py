# Create a list containing integers from 1 to 10.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the length of the list.
print("List length: ", len(my_list))

# Access and print an element at index 1.
print(f"List indexing: {my_list[1]}")

# Slice the list from index 2 to the end and print the result.
print(f"List slicing: {my_list[2:]}")

# Slice the list from index 1 to 5 and print the result.
print(f"List slicing 2: {my_list[1:6]}")

# Slice the list from index 1 to 8 with a step of 2 and print the result.
print(f"List slicing 3: {my_list[1:8:2]}")

# Slice the list in reverse order and print the result.
print(f"List slicing 4: {my_list[-2:1:-3]}")

# Modify the first element of the list.
my_list[0] = 17
print(f"Lists are mutable, i.e: {my_list}")
my_list[0] = 1  # Restore the original value

# Append a new element to the end of the list.
my_list.append(11)
print(f"List appending: {my_list[10]}")

# Pop the last element from the list and assign it to a variable.
num = my_list.pop()
print(f"List popping: You can assign the deleted value to a new variable. I.e: {num}")
print(f"List popping 2: {my_list} (Number 11 has been removed)")

# Reverse the order of elements in the list.
my_list.reverse()
print(f"List reversing: {my_list}")

# Create a list of integers.
list_1 = [5, 3, 6, 1, 2, 4]

# Sort the list in ascending order.
print(f"List before sort: {list_1}")
list_1.sort()
print(f"List after sorting: {list_1}")

# Create a list of characters.
list_2 = ['b', 'a', 'd', 'c']

# Sort the list in ascending order (alphabetically).
print(f"List before sort: {list_2}")
list_2.sort()
print(f"List after sorting 2: {list_2}")

# Create a list of integers.
list_3 = [1, 2, 3, 4, 5]

# Reverse the list in-place and then sort it in ascending order.
list_3[::-1].sort()
print(list_3)
