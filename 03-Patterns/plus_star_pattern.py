rows=int(input("Enter odd number of rows: "))
mid=rows//2

for i in range(rows):
    for j in range(rows):
        if i==mid or j==mid:
            print("*", end="")
        else:
            print(" ", end="")
    print()            