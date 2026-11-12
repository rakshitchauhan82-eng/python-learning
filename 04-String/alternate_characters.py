input_str = input("Enter a string: ")
result = ""

for i in range(0, len(input_str), 2):
    result += input_str[i]

print(f"Alternate characters: {result}")