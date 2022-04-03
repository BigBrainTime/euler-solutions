start = [3, 5]
list = []

for i in reversed(range(1000)):
    for k in range(len(start)):
        if i % start[k] == 0 and i % start[k] not in list:
            list.append(i)
            break

print(sum(list))