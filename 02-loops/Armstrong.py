num=int(input("Enter a number:"))
pov=len(str(num))
arm=num
sum=0
ld=0
while num>0:
    ld=num%10
    sum=sum +ld**pov
    num=num//10

if sum == arm :
    print("{} is armstrong !".format(sum))
else:
    print("{} is not armstrong !".format(sum))  

