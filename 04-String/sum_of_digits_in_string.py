input_str = input("Enter a string: ")
total = 0

for i in input_str:
    if i.isdigit():
        total += int(i)

print(f"Sum of digits is: {total}")
