input_str = input("Enter a string: ")
char_to_find = input("Enter a character to find its frequency: ")
count = 0

for i in input_str:
    if i == char_to_find:
        count += 1

if count == 0:
    print(f"{char_to_find} is not present in the string ") 
else:           
    print(f"Frequency of {char_to_find} is {count}")

     



