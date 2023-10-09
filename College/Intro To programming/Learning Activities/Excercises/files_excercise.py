my_file = open("Learning Activities\\textfiles\\myfile.txt", mode="w")
my_file.write("Hello, World")
my_file.close()

with open("Learning Activities\\textfiles\\myfile.txt", mode="w") as my_data:
    my_data.write("Hello World")

with open("Learning Activities\\textfiles\\myfile.txt", mode="a") as my_data:
    my_data.write("\nHobbies:\n\tCoding\n\tGaming\n\tListening to music")