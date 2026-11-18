input_str1 = input("Enter first string: ")
input_str2 = input("Enter second string: ")

if len(input_str1) == len(input_str2) and input_str2 in input_str1 + input_str1:
    print("Second string is a rotation of the first string")
else:
    print("Second string is not a rotation of the first string")