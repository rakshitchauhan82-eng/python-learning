n=int(input('Enter a number: '))
fact=[]
for i in range(1,n+1):
    if n%i==0:
        fact.append(i)
print("Factors of {} are {}".format(n,fact))