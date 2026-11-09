input_str = input("Enter a string: ")
words = input_str.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print(f"String after capitalizing: {result.strip()}")