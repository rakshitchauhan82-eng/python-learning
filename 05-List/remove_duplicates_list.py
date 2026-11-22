numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print(f"List after removing duplicates: {unique}")