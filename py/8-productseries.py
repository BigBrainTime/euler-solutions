import math
import RequestPull

raw = RequestPull.pull(8)
big_number = ''
for num in raw:
    big_number += str(num)

high = 0
tem = []
ad = 13

for n in big_number:
    if len(tem) >= ad:
        del tem[0]

    tem.append(int(n))

    temp = math.prod(tem)

    if temp > high:
        high = temp

print(high)