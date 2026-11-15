input_str = input("Enter a string: ")
length = int(input("Enter the length: "))
words = input_str.split()
count = 0

for i in words:
    if len(i) == length:
        count += 1

print(f"Number of words with length {length}: {count}")