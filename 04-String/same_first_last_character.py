input_str = input("Enter a string: ")

if input_str == "":
    print("String is empty!")
elif input_str[0] == input_str[-1]:
    print("First and last characters are same")
else:
    print("First and last characters are not same")        