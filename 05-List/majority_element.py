numbers = list(map(int, input("Enter numbers separated by space: ").split()))

candidate = None
count = 0

for i in numbers:
    if count == 0:
        candidate = i
        count = 1
    elif i == candidate:
        count += 1
    else:
        count -= 1

if candidate is not None and numbers.count(candidate) > len(numbers) // 2:
    print(f"Majority element is: {candidate}")
else:
    print("No majority element")