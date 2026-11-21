numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even numbers: {even}")
print(f"Odd numbers: {odd}")