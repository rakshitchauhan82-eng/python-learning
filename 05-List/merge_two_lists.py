list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
merged = []

for i in list1:
    merged.append(i)

for i in list2:
    merged.append(i)

print(f"Merged list is: {merged}")