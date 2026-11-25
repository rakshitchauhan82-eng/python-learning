rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

print("Transpose of the matrix:")

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()