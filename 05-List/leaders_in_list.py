numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    leaders = []
    max_right = numbers[-1]
    leaders = [max_right]

    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] > max_right:
            max_right = numbers[i]
            leaders = [max_right] + leaders

    print(f"Leaders are: {leaders}")