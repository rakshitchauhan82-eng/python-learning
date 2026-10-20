num=int(input("Enter a number: "))
power=int(input("Enter terms in power: "))
result=1

for i in range(1, abs(power) + 1):
    result *= num

if power < 0:
    if result==0:
        print("Zero cannot have a negative power!")

    else:
        result=1/result
        print("Power of {} is {}".format(num,result))        

print("Power of {} is {}".format(num,result))