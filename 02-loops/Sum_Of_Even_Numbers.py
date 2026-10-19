num=int(input("Enter a range (1 to n): "))
sum=0
for i in range(1,num+1):
    if i % 2 == 0 :
        sum+=i
    else:
        continue 

print("Sum of Even numbers are {}".format(sum))