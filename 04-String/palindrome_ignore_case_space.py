input_str = input("Enter a string: ")
cleaned = ""

for i in input_str:
    if i.isalnum():
        cleaned += i.lower()

rev_str = ""
for i in cleaned:
    rev_str = i + rev_str

if cleaned == rev_str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
    