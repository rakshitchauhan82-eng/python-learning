num=input("Enter Numbers separated by space: ").split()

smallest = int(num[0])

for i in num:
    if int(i) < smallest :
        smallest = i
    
    else:
        continue

print("Smallest number is {}".format(smallest))   