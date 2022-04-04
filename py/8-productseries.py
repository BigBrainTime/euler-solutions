import math
import urllib.request

link = ("https://projecteuler.net/minimal=8")
raw = []

with urllib.request.urlopen(link) as url:
    data = url.readlines()
data.pop()
for i in range(2):
    data.pop(0)

for num in data:
    raw.append(str(num).replace("<br />\\n'", '').replace("b'","").replace("<br /></p>\\n'",""))
big_number = ''
for num in raw:
    big_number += num

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