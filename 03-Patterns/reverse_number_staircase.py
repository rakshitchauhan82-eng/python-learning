rows=int(input("Enter number of rows: "))

for k in range(1, rows+1):
    print(" " * (rows - k), end="")
    for l in range(k, 0, -1):
        print(l, end="")
    print()