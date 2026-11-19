input_str = input("Enter a string: ")
digits = ""

for i in input_str:
    if i.isdigit():
        digits += i

print(f"Digits in the string: {digits}")