input_str1 = input("Enter first string: ").lower()
input_str2 = input("Enter second string: ").lower()

if sorted(input_str1) == sorted(input_str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")