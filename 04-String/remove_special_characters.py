input_str = input("Enter a string: ")
result = ""

for i in input_str:
    if i.isalnum() or i == " ":
        result += i

print(f"String after removing special characters: {result}")