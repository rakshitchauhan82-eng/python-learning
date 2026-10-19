num=int(input("Enter a Range (1 to n) : "))
even=[]
odd=[]
for i in range(1,num):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Evens are {}".format(even))
print( )
print("Odds are {}".format(odd))           
