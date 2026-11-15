input_str = input("Enter a string: ")

for i in range(1, len(input_str) + 1):
    for j in range(i):
        print(input_str[j], end="")
    print()