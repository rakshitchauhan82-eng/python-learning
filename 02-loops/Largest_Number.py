numbers = input("Enter numbers: ").split()

largest = int(numbers[0])

for n in numbers:
    if int(n) > largest:
        largest = int(n)

print("Largest number is: {}".format( largest) )      
