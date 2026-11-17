input_str = input("Enter a string: ")

if len(input_str) < 3:
    print("String is too short")
else:
    result = input_str[1:-1]
    print(f"String after removing first and last character: {result}")