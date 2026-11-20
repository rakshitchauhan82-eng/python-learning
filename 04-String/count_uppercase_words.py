input_str = input("Enter a string: ")
words = input_str.split()
count = 0

for word in words:
    if word.isupper():
        count += 1

print(f"Number of uppercase words: {count}")