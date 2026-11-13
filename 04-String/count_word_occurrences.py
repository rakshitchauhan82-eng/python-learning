input_str = input("Enter a string: ")
word_to_find = input("Enter word to find: ")
count = 0

for i in input_str.split():
    if i == word_to_find:
        count += 1

print(f"{word_to_find} appears {count} times")
