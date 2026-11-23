numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = None
second = None

for i in numbers:
    if largest is None or i > largest:
        if largest is not None:
            second = largest
        largest = i
    elif i != largest and (second is None or i > second):
        second = i

if second is None:
    print("No second largest number")
else:
    print(f"Second largest number is: {second}")