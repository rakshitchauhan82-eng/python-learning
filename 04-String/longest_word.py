input_str = input("Enter a string: ")
words = input_str.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(f"Longest word is: {longest}")