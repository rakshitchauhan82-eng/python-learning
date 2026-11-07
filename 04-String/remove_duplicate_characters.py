input_str = input("Enter a string: ")
no_duplicate = ""

for i in input_str:
    if i not in no_duplicate:
        no_duplicate += i
print(f"String after removing duplicate characters: {no_duplicate}")