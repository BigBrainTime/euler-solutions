numbers = []

for i in range(1000000):
    sep = list(map(int, str(i)))
    binarysep = list(map(int, bin(i)[2:]))
    if sep == list(reversed(sep)) and binarysep == list(reversed(binarysep)):
        numbers.append(i)

print(sum(numbers))