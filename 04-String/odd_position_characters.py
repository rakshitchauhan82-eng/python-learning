input_str = input("Enter a string: ")
result = ""

for i in range(1, len(input_str), 2):
    result += input_str[i]

print(f"Odd position characters: {result}")