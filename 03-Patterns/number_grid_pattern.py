rows=int(input("Enter number of rows: "))
a=1

for i in range(1, rows+1):
    for j in range(1, rows+1):
        print(a, end=" ")
        a+=1
    print()        