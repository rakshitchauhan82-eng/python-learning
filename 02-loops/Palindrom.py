num=int(input("Enter a number: "))
last_digit=0
reverse=0
original=num

while num>0:
    last_digit=num%10
    reverse=reverse*10+last_digit
    num//=10

if reverse==original:
    print("{} is Palindrom!".format(reverse)) 
else :
    print("{} is not Palindrom!".format(reverse))

