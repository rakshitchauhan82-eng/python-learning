rows=int(input("Enter number of rows: "))

for i in range(rows):
    print(" " * (rows - i - 1), end="")

    c=1

    for j in range(i+1):
        print(c, end=" ")

        c = c * (i - j) // (j + 1)

    print()    