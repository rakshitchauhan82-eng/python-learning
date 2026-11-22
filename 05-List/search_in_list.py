numbers = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter number to search: "))
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"{target} is found at position {i}")
        found = True
        break

if not found:
    print(f"{target} is not found in the list")