start = [3, 5]
list = []

for i in reversed(range(1000)):
    for value in start:
        if i % value == 0 and i % value not in list:
            list.append(i)
            break

print(sum(list))