rows=int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(2 * i - 1):
        if i==rows or j==0 or j==2*i-2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for k in range(2, rows+1):
    print(" " * (rows - k), end="")
    for l in range(2 * k - 1):
        if k==rows or l==0 or l==2*k-2:
            print("*", end="")
        else:
            print(" ", end="")
    print()        