upper=int(input("Enter uper limit: "))
lower=int(input("Enter lower limit: "))
primes=[]

for i in range(upper,lower):
    if i > 1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            primes.append(i)
print("Primes in range are {}".format(primes))
