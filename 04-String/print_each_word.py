input_str = input("Enter a string: ")
words = input_str.split()

for i in words:
    print(f"{i} = {len(i)}")