list = []

def thr(x):
    global list

    remainder = x % 3
    is_divisible = remainder == 0

    if is_divisible == True:
        list.append(x)

def fiv(x):
    global list

    remainder = x % 5
    is_divisible = remainder == 0

    if is_divisible == True and x not in list:
        list.append(x)

for i in range(1000):
    thr(i)
    fiv(i)

print(sum(list))