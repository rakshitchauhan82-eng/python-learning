num=int(input("Enter a number:"))
factors=[]

for i in range(1,num):
    if num%i==0:
        factors.append(i)

perfect_number=sum(factors)

if perfect_number == num:
    print("{} is Perfect number".format(num))

else:
    print("{} is not Perfect number!".format(num))    