n = int(input("Enter size of the square matrix: "))
matrix = []

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

print("Matrix after rotating:")

for j in range(n):
    for i in range(n - 1, -1, -1):
        print(matrix[i][j], end=" ")
    print()