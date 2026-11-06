input_str = input("Enter a string: ")
chr_freq = ""

for chr in input_str:
    if chr not in chr_freq:
        print(f"Frequency of {chr} is : {input_str.count(chr)}")
        chr_freq += chr 