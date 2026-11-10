input_str = input("Enter a string: ")
char_to_remove = input("Enter a character to remove: ")
result = ""

for i in input_str:
    if i != char_to_remove:
        result += i

print(f"String after removing {char_to_remove}: {result}")