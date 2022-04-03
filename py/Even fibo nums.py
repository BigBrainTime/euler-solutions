list = [1, 2]
list2 = []
it = 0
check = 1


while check == 1:
    num = list[it] + list[it+1]

    if num < 4000000:
        list.append(num)

    else:
        for i in range(len(list)):
            remainder = list[i]%2
            is_divisible = remainder == 0

            if is_divisible == True:
                list2.append(list[i])

        print(sum(list2))
        check = 0
    it = it + 1