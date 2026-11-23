numbers = list(map(int, input("Enter numbers separated by space: ").split()))
is_sorted = True

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i-1]:
        is_sorted = False
        break

if is_sorted:
    print("List is sorted")
else:
    print("List is not sorted")