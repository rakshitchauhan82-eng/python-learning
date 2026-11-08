input_str = input("Enter a string: ")
result = ""

for i in input_str:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()
    else:
        result += i

print(f"String after toggling case: {result}")