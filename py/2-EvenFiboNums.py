list = [1, 2]
total = 0
it = 0
num=0

while num < 4000000:
    num = list[it] + list[it+1]

    list.append(num)
    total += num*int(not bool(num%2))

    it += 1

print(total)