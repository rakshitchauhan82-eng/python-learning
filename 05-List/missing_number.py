numbers = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = 0

for i in numbers:
    actual_sum += i

print(f"Missing number is: {expected_sum - actual_sum}")