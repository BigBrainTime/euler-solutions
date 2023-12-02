high = 0

for i in reversed(range(1000)):
    for k in reversed(range(1000)):
        if i * k > high:
            sep = list(map(int, str(i * k)))
            if sep == list(reversed(sep)):
                high = i * k

print(high)