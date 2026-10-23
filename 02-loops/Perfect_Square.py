num=int(input("Enter a number : "))
x=1
while  x*x<=num:
    if x*x==num:
        print("{} is Perfect square".format(num))
        break
    x+=1
else:
    print("{} is not a Perfect square".format(num))