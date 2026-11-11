input_str = input("Enter a string: ")
count = 0

for i in input_str:
    if i == " ":
        count += 1

print(f"Number of spaces: {count}")