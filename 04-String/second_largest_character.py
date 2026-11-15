input_str = input("Enter a string: ")

largest = ""
second = ""

for i in input_str:
    if largest == "" or i > largest:
        if largest != "":
            second = largest
        largest = i
    elif i != largest and (second == "" or i > second):
        second = i

if second == "":
    print("No second largest character")
else:
    print(f"Second largest character is: {second}")