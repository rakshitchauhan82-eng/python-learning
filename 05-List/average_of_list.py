numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    total = 0

    for i in numbers:
        total += i

    average = total / len(numbers)
    print(f"Average of the list is: {average}")