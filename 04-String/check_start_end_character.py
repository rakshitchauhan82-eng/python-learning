input_str = input("Enter a string: ")
ch = input("Enter a character: ")

if input_str == "":
    print("String is empty")
elif input_str[0] == ch and input_str[-1] == ch:
    print(f"String starts and ends with {ch}")
else:
    print(f"String does not start and end with {ch}")