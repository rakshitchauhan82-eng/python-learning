input_str = input("Enter a string: ")

if input_str == "":
    print("The string is empty")

else:
    smallest_chr = input_str[0]

    for i in input_str:
        if i < smallest_chr:
            smallest_chr = i

    print(f"Smallest character is: {smallest_chr}")        