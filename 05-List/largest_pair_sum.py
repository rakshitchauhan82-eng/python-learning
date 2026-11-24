numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) < 2:
    print("List needs at least 2 numbers")
else:
    first = max_first = numbers[0]
    second = numbers[1]

    if second > first:
        first, second = second, first

    for i in range(2, len(numbers)):
        if numbers[i] > first:
            second = first
            first = numbers[i]
        elif numbers[i] > second:
            second = numbers[i]

    print(f"Largest two numbers: {first} and {second}")
    print(f"Sum: {first + second}")