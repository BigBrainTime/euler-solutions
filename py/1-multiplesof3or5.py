start = [3, 5]
list = []

for i in range(1000):
    for value in start:
        if i % value == 0:
            list.append(i)
            break

print(sum(list))