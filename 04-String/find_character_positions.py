input_str = input("Enter a string: ")
char_to_find = input("Enter a character to find: ")
found = False

print(f"{char_to_find} is present at positions:", end=" ")

for i in range(len(input_str)):
    if input_str[i] == char_to_find:
        print(i, end=" ")
        found = True

if not found:
    print("nowhere (character not found)")
    