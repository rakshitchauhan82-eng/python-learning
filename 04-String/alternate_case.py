input_str = input("Enter a string: ")
result = ""

for i in range(len(input_str)):
    if i % 2 == 0:
        result += input_str[i].upper()
    else:
        result += input_str[i].lower()

print(f"String after alternating case: {result}")