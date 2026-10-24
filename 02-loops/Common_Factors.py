num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

common_factors=[]

for i in range (1,num2+1):
    if num1%i == 0 and num2%i == 0 :
        common_factors.append(i)

print("Common divisors of {} & {} are {}".format(num1,num2,common_factors))