list = [1, 1]
it = 0
num=2

while len(str(num)) < 1000:
    num = list[it] + list[it+1]
    list.append(num)

    it += 1

print(list.index(num)+1)