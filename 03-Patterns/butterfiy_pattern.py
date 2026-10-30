n=int(input("Enter number of rows:"))

for i in range(1,n+1):  
    for j in range(1,i+1):    
        print("*",end="" )  
    print(" " * 2 * (n-i), end="")
    for k in range(1,i+1):
        print("*",end="" )
    print()   
     
for l in range(k-1,0,-1):
    for m in range(l,0,-1):
        print("*",end="")
    print(" " * 2 * (n-l), end="")   
    for o in range(l,0,-1):
        print("*", end="")
    print()       

