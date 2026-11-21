numbers = list(map(int, input("Enter numbers separated by space: ").split()))
rev_list = []

for i in numbers:
    rev_list = [i] + rev_list

print(f"Reversed list is: {rev_list}")