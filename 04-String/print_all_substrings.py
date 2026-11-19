input_str = input("Enter a string: ")

for i in range(len(input_str)):
    for j in range(i + 1, len(input_str) + 1):
        print(input_str[i:j])