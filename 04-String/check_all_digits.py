input_str = input("Enter a string: ")
only_digits = True

if input_str == "":
    only_digits = False

for i in input_str:
    if not i.isdigit():
        only_digits = False
        break

if only_digits:
    print("String contains only digits")
else:
    print("String does not contain only digits")