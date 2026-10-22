num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
common_divisors=[]

for i in range(1,num2):
    if num1%i==0 and num2%i==0:
        common_divisors.append(i)

gcd=int(common_divisors[0])

for j in common_divisors:
    if int(j) > gcd:
        gcd = int(j)
print("Greatest Common Divisor is {}".format(gcd))        
    
