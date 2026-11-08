input_str = input("Enter a string: ")
result = ""

for i in input_str:
    if i.lower() not in "aeiou":
        result += i

print(f"String after removing vowels: {result}")
