input_str = input("Enter a string: ")
only_alpha = True

if input_str == "":
    only_alpha = False

for i in input_str:
    if not i.isalpha():
        only_alpha = False
        break

if only_alpha:
    print("String contains only alphabets")
else:
    print("String does not contain only alphabets")