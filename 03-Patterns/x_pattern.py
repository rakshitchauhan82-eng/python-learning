rows=int(input("Enter number of rows: "))

for i in range(1, rows+1):
    for j in range(1, i+1):
        if i==j:
            print("*", end="")
        else:
            print(" ", end="")

    print(" " * 2 * (rows-i), end="")  

    for k in range(i, 0, -1):
        if k==i:
            print("*", end="")
        else: 
            print(" ", end="")   
    print()    

for l in range(rows-1, 0, -1):
    for m in range(1, l+1):
        if m==l:
            print("*", end="")
        else:
            print(" ", end="")

    print(" " * 2 * (rows-l), end="") 

    for o in range(l, 0, -1):
        if o==l :
            print("*", end="")
        else:
            print(" ", end="")
    
    print()            
