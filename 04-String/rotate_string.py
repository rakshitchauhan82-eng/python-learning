input_str = input("Enter a string: ")

if input_str == "":
    print("String is empty")
else:
    result = input_str[1:] + input_str[0]
    print(f"String after rotating: {result}")