input_str = input("Enter a string: ").lower()
count = 0

for i in input_str:
    if i.isalpha() and i not in "aeiou":
        count += 1

print(f"Number of consonants: {count}")