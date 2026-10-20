s=input("Enter a string: ")
vowel='aieou'
count=0

for i in s:
    if i.lower() in vowel :
        count+=1
    else:
        continue    

print("Number of vowels are {}".format(count))