input_str = input("Enter a string: ").lower()
done = ""

print("Vowels in the string:", end=" ")

for i in input_str:
    if i in "aeiou" and i not in done:
        print(i, end=" ")
        done += i