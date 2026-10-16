a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>b and a>c:
    print(f"{a} : number is greatest number")
elif b>a and b>c:
    print(f"{b} : number is greatest number")
elif c>a and c>b:
    print(f"{c} : number is greatest number") 
else:
    print("All numbers are equal") 