input_str = input("Enter a string: ")
found = False

for i in input_str:
    if i.isdigit():
        found = True
        break

if found:
    print("String contains digits")

else:
    print("String does not contain digits")