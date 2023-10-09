# data = open("Learning Activities\\textfiles\\hello.txt")
# print(data.read())

# data.seek(22)
# print(f"Data seek: {data.read()}")

# data.seek(0)
# print(f"Data Read lines: {data.readlines()}")

# data.seek(0)
# lines = data.readlines()
# print(lines[0])

# data.close()

with open("Learning Activities\\textfiles\\hello.txt", mode="w+") as my_data:
    my_data.write("This is the second line")
    my_data.seek(0)
    print(my_data.read())

print("Out of with")
