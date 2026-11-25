numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    longest = 1
    current = 1

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    print(f"Length of longest increasing run: {longest}")