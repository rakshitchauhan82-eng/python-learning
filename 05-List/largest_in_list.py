numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    largest = numbers[0]

    for i in numbers:
        if i > largest:
            largest = i

    print(f"Largest number is: {largest}")