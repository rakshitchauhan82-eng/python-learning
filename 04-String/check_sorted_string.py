input_str = input("Enter a string: ")
is_sorted = True

for i in range(1, len(input_str)):
    if input_str[i] < input_str[i-1]:
        is_sorted = False
        break

if is_sorted:
    print("String is in alphabetical order")
else:
    print("String is not in alphabetical order")
    