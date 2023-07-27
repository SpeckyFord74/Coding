user_input = int(input("Enter an integer: "))

odd_or_even = user_input % 2

if odd_or_even == 0:
    print(f"The number {user_input} is even")

elif odd_or_even != 0:
    print(f"The number {user_input} is odd")