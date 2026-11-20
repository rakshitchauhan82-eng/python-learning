input_str = input("Enter a string: ")
ch = input("Enter a character to insert: ")
result = ""

for i in range(len(input_str)):
    result += input_str[i]
    if i != len(input_str) - 1:
        result += ch

print(f"String after inserting: {result}")