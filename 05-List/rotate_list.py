numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter number of positions: "))

if len(numbers) == 0:
    print("List is empty")
else:
    k = k % len(numbers)
    rotated = numbers[k:] + numbers[:k]
    print(f"List after rotating: {rotated}")