input_str = input("Enter a string: ").lower()
is_isogram = True

for i in input_str:
    if i.isalpha() and input_str.count(i) > 1:
        is_isogram = False
        break

if is_isogram:
    print("String is an isogram")
else:
    print("String is not an isogram")