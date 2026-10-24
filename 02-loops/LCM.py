num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

m1 = []
m2 = []

for i in range(1, num2 + 1):
    m1.append(i * num1)

for j in range(1, num1 + 1):
    m2.append(j * num2)

for lcm1 in m1:
    if lcm1 in m2:
        print("LCM is {}".format(lcm1))
        break

    