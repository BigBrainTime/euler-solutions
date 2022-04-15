#In progress
found = []

for i in range(1,10000):
    if i not in found:
        tem = 0
        temp = 0

        for k in range(1,i//2+1):
            if i % k == 0:
                tem += k

        for n in range(1,tem//2+1):
            if i % n == 0:
                temp += n

        if temp == i:
            print(i,tem,temp)
            found.append(tem)
            found.append(temp)

print(sum(found))