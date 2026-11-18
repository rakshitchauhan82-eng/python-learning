input_str = input("Enter a string: ")
found = False

for i in input_str:
    if input_str.count(i) == 1:
        print(f"First non-repeating character is: {i}")
        found = True
        break

if not found:
    print("No non-repeating character")