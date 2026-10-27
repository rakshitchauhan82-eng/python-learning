start=int(input("Enter start range: "))
end=int(input("Enter end range: "))
for num in range(start,end+1):
    pov=len(str(num))
    arm=num
    sum=0
    

    while arm > 0:
        ld = arm % 10
        sum = sum + ld ** pov
        arm = arm // 10

    if sum == num :
        print("Armstrong numbers in range are {}".format(num))