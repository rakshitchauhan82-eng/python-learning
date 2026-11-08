input_str = input("Enter a string: ")
upper_count = 0
lower_count = 0

for i in input_str:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
