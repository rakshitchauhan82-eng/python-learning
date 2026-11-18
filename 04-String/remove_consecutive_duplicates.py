input_str = input("Enter a string: ")
result = ""

for i in input_str:
    if result == "" or i != result[-1]:
        result += i

print(f"String after removing consecutive duplicates: {result}")