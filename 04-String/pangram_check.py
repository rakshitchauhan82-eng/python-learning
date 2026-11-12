input_str = input("Enter a string: ").lower()
alphabets = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for i in alphabets:
    if i not in input_str:
        is_pangram = False
        break

if is_pangram:
    print("String is a pangram")
else:
    print("String is not a pangram")