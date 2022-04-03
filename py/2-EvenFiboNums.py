list = [1, 2]
list2 = []
it = 0
check = True


while check:
    num = list[it] + list[it+1]

    if num < 4000000:
        list.append(num)
        if num%2 == 0:
            list2.append(num)

    else:
        print(sum(list2))
        check = False
    it += 1