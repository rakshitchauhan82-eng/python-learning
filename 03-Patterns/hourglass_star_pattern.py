rows=int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(2*i-1):
        print("*", end="")
    print() 

for k in range(2, rows+1):
    print(" " * (rows - k), end="")
    for l in range(2*k-1):
        print("*", end="")
    print()            