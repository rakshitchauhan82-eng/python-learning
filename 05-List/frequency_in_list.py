numbers = list(map(int, input("Enter numbers separated by space: ").split()))
done = []

for i in numbers:
    if i not in done:
        print(f"{i} = {numbers.count(i)}")
        done.append(i)