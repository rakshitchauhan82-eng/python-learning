n = int(input("Enter size of the square matrix: "))
matrix = []

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

main_sum = 0
other_sum = 0

for i in range(n):
    main_sum += matrix[i][i]
    other_sum += matrix[i][n - 1 - i]

print(f"Main diagonal sum: {main_sum}")
print(f"Other diagonal sum: {other_sum}")