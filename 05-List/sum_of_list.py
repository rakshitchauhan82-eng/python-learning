numbers = list(map(int, input("Enter numbers separated by space: ").split()))
total = 0

for i in numbers:
    total += i

print(f"Sum of the list is: {total}")