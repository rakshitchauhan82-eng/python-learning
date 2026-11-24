numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for i in range(len(numbers)):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"Sorted list is: {numbers}")
