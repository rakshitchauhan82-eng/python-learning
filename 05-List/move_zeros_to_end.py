numbers = list(map(int, input("Enter numbers separated by space: ").split()))
result = []
zeros = 0

for i in numbers:
    if i == 0:
        zeros += 1
    else:
        result.append(i)

for i in range(zeros):
    result.append(0)

print(f"List after moving zeros: {result}")