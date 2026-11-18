input_str = input("Enter a string: ")
sub = input("Enter a substring: ")
count = 0

if sub == "":
    print("Substring is empty")
else:
    for i in range(len(input_str) - len(sub) + 1):
        if input_str[i:i+len(sub)] == sub:
            count += 1

    print(f"{sub} appears {count} times")