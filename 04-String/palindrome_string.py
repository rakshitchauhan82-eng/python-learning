input_str = input("Enter a string: ")
rev_str = ""

for i in input_str:
    rev_str = i + rev_str

if input_str == rev_str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")