input_str = input("Enter a string: ")

if input_str == "":
    print("String is empty")

else:
    largest_chr = input_str[0]

    for ch in input_str:
        if ch > largest_chr:
            largest_chr = ch
            
    print(f"Largest character in the string is: {largest_chr}")