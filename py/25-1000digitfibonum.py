list = [1, 1]
it = 0
check = True

while check:
    num = list[it] + list[it+1]
    list.append(num)
    if len(str(num)) >= 1000:
        print(list.index(num)+1)
        check = False

    it += 1