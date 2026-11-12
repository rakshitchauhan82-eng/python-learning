input_str = input("Enter a string: ")
result = ""

for i in input_str:
    if i.lower() in "aeiou":
        result += "*"
    else:
        result +=i 
print(f"String after replacing vowels: {result}")
           