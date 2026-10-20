num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result=0

for i in range(1, abs(num2) + 1):
    result+=num1

if num2<0:
    result=-result

print(result)