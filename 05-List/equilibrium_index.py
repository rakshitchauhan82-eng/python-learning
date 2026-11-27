numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for i in numbers:
    total += i

left = 0
found = False

for i in range(len(numbers)):
    right = total - left - numbers[i]

    if left == right:
        print(f"Equilibrium index is: {i}")
        found = True
        break

    left += numbers[i]

if not found:
    print("No equilibrium index")