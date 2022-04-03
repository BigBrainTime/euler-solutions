data = []
high = 0
br = 950  #early break to shorten run time

for i in reversed(range(1000)):
    for k in reversed(range(1000)):
        if i * k not in data and i * k > high:
            sep = list(map(int, str(i * k)))
            data.append(i * k)

            if sep == list(reversed(sep)):
                high = i * k
        elif k < br:
            break
    if i < br:
        break

print(high)