input_str = input("Enter a string: ")
words = input_str.split()
result = ""

for i in words:
    rev_word = ""
    for j in i:
        rev_word = j + rev_word
    result += rev_word + " "

print(f"String after reversing each word: {result.strip()}")