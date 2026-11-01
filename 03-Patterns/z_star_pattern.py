rows=int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        if i==0 or i==rows-1 or j==rows-1-i :
            print("*", end="")
        else:
            print(" ", end="")
    print()         