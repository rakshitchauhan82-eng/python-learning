input_str = input("Enter a string: ")
words = input_str.split()
shortest = words[0]

for i in words:
    if len(i) < len(shortest):
        shortest = i

print(f"Shortest word is: {shortest}")

