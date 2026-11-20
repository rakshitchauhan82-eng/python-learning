input_str = input("Enter a string: ")
ch = input("Enter a letter: ")
words = input_str.split()
count = 0

for word in words:
    if word[-1].lower() == ch.lower():
        count += 1

print(f"Number of words ending with {ch}: {count}")