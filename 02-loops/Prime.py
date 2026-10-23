num=int(input("Enter a number:"))
count=0
for i in range (2,num):
    if num%i==0:
        print("{} is not prime number".format(num))
        break
else:
     print("{} is prime number".format(num))  