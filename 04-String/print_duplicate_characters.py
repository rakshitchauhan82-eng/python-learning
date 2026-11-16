input_str = input("Enter a string: ")
done = ""

print("Duplicate characters:", end=" ")

for i in input_str:
    if input_str.count(i) > 1 and i not in done:
        print(i, end=" ")
        done += i