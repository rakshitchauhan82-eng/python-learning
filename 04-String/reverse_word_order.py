input_str = input("Enter a string: ")
words = input_str.split()
result = ""

for i in words:
    result = i + " " + result

print(f"String after reversing word order: {result.strip()}")