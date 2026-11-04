rows=int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(i):
        print("*", end="")
    print()

for k in range(rows-1, 0, -1):
    for l in range(k):
        print("*", end="")
    print()