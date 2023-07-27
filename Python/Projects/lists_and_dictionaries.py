student1_name = input("Enter the first students name: ")
student1_age = int(input("Enter the first students age: "))
student1_major = input("Enter the first students major: ")

student2_name = input("Enter the second students name: ")
student2_age = int(input("Enter the second students age: "))
student2_major = input("Enter the second students major: ")

student3_name = input("Enter the third students name: ")
student3_age = int(input("Enter the third students age: "))
student3_major = input("Enter the third students major: ")

students = [
    {"Name": f"{student1_name}", "Age": f"{student1_age}", "Major": f"{student1_major}"},
    {"Name": f"{student2_name}", "Age": f"{student2_age}", "Major": f"{student2_major}"},
    {"Name": f"{student3_name}", "Age": f"{student3_age}", "Major": f"{student3_major}"},
]

for student in students:
    print(f"Student:")
    print("Name: ", student["Name"])
    print("Age: ", student["Age"])
    print("Major: ", student["Major"], "\n")
