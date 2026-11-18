input_str = input("Enter a string: ")
shift = 3
result = ""

for i in input_str:
    if i.isupper():
        result += chr((ord(i) - 65 + shift) % 26 + 65)
    elif i.islower():
        result += chr((ord(i) - 97 + shift) % 26 + 97)
    else:
        result += i

print(f"Encrypted string: {result}")