input_str = input("Enter a string: ")
result = ""

for i in input_str:
    if not i.isdigit():
        result += i
print(f"String after removing digits: {result}")        