numbers = list(map(int, input("Enter sorted numbers separated by space: ").split()))
target = int(input("Enter number to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print(f"{target} is found at position {mid}")
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(f"{target} is not found in the list")