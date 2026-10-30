rows=int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        if i==rows or j==1 or i==j : 
            print("*", end="")
        else:
            print(" ", end="")    
    print()             