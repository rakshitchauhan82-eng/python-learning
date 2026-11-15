input_str = input("Enter a string: ").lower()

for i in "aeiou":
    count = 0
    for i in input_str:
        if i == i:
            count += 1
    print(f"{i} = {count}")