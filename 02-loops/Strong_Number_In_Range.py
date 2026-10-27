start=int(input("Enter start of range: "))
end=int(input("Enter end of range: "))

for num in range(start,end+1):
    temp=num
    total=0

    while temp > 0:
        digit = temp % 10

        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        temp = temp // 10

    if total == num:
        print("Strong numbers in range are {}".format(num))
else :
        print("There are no strong number in range")    