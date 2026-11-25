numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    current = numbers[0]
    best = numbers[0]

    for i in range(1, len(numbers)):
        if current + numbers[i] > numbers[i]:
            current += numbers[i]
        else:
            current = numbers[i]

        if current > best:
            best = current

    print(f"Maximum subarray sum is: {best}")