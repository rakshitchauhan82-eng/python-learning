input_str = input("Enter a string: ")
words = input_str.split()

if len(words) == 0:
    print("String is empty")
else:
    largest = words[0]

    for word in words:
        if word > largest:
            largest = word

    print(f"Largest word is: {largest}")