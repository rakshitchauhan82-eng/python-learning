input_str = input("Enter a string: ")

print("Unique characters:", end=" ")

for i in input_str:
    if input_str.count(i) == 1:
        print(i, end=" ")