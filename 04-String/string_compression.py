input_str = input("Enter a string: ")

if input_str == "":
    print("String is empty")
else:
    result = ""
    count = 1

    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i-1]:
            count += 1
        else:
            result += input_str[i-1] + str(count)
            count = 1

    result += input_str[-1] + str(count)

    print(f"Compressed string: {result}")