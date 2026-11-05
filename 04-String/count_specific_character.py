user_input = input("Enter a string: ")
character = input("Enter a character: ")

for i in user_input:
    if i==character:
        print(f"{character} is present in the string")