numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    smallest = numbers[0]

    for i in numbers:
        if i < smallest:
            smallest = i

    print(f"Smallest number is: {smallest}")
