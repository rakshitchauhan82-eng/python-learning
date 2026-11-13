input_str = input("Enter a string: ")

if len(input_str) < 2:
    print(f"String after swapping: {input_str}")
else:
    result = input_str[-1] + input_str[1:-1] + input_str[0]
    print(f"String after swapping: {result}")    
