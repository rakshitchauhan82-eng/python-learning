input_str = input("Enter a string: ").lower()
vowels = 0
consonants = 0

for i in input_str:
    if i.isalpha():
        if i in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")