data = []
high = 0

for i in reversed(range(1000)):
    for k in reversed(range(1000)):
        mul = i * k

        if mul not in data and mul > high:
            sep = []

            for l in range(len(str(mul))): 
                sep.append(str(mul)[l])

            if sep == list(reversed(sep)):
                print(mul,' has passed')
                high = mul

            data.append(mul)

print(high)