start=int(input("Enter start range: "))
end=int(input("Enter end range: "))

for num in range(start,end+1):
    temp=num
    factors=[]

    for i in range(1,temp):
        if num%i==0:
            factors.append(i)

    perfect_number=sum(factors)

    if perfect_number == num:   
        print("Perfect number in range are {}".format(num))

