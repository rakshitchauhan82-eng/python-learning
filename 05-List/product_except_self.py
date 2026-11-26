numbers = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(numbers)
result = [1] * n

left = 1
for i in range(n):
    result[i] = left
    left *= numbers[i]

right = 1
for i in range(n - 1, -1, -1):
    result[i] *= right
    right *= numbers[i]

print(f"Result: {result}")