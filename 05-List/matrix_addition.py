rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix1 = []
matrix2 = []

print("Enter first matrix:")
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix1.append(row)

print("Enter second matrix:")
for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix2.append(row)

print("Sum of the matrices:")

for i in range(rows):
    for j in range(cols):
        print(matrix1[i][j] + matrix2[i][j], end=" ")
    print()