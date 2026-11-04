rows=int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")
    print(" " * 2 * (rows-i), end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()