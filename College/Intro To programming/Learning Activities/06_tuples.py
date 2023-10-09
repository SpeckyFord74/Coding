my_tuple = (1,2,3,4,5)
print(my_tuple)

print(len(my_tuple))

my_tuple_1 = ('a',1,'b',2,'c',3)
print(my_tuple_1)
print(len(my_tuple_1))

print(f"Slicing 1: {my_tuple_1[1:4:1]}")
print(f"Slicing 2: {my_tuple_1[1:6:2]}")
print(f"Slicing 3: {my_tuple_1[1:-1:1]}")
print(f"Indexing 1: {my_tuple_1[0]}")
print(f"Indexing 2: {my_tuple_1[-1]}")
print(f"Functions 1: {my_tuple_1.index('b')}")
print(f"Functions 2: {my_tuple_1.count(2)}")

joined_tuple = my_tuple + my_tuple_1
print(joined_tuple)

my_tuple1 = (1,2,[1,2])
my_tuple1[2][0] = 2
print(my_tuple1[2])