input_str1 = input("Enter first string: ")
input_str2 = input("Enter second string: ")

result = True

if len(input_str1) != len(input_str2):
    result = False

else:
    for  i in range(len(input_str1)):
        if input_str1[i] != input_str2[i]:
            result = False
            break

if result:
    print("Both strings are equal")
else:
    print("Both strings are not same")  