input_str = input("Enter a string: ")
letters = 0
digits = 0

for i in input_str:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")