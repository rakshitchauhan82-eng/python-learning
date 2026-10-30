n=int(input("Enter number of rows: "))

for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(2 * i - 1):
        if j==0 or j==2*i-2  :
            print("*", end="")
        else:
            print(" ", end="")    
    print()

for k in range(n-1, 0, -1):
    print(" " * (n-k), end="")
    for l in range(2*k-1, 0, -1):
        if l==2*k-1 or l==1:
            print("*", end="")      
        else:
            print(" ", end="")
    print()    