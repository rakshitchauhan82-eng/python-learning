input_str = input("Enter a string: ")
words = input_str.split()
count = 0

for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print(f"Words starting with a vowel: {count}")