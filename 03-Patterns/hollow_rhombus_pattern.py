rows=int(input("Enter number of rows: "))

for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, rows+1):
        if i==1 or i==rows or j==1 or j==rows:
            print("*", end="")
        else:
            print(" ", end="")
    print() 