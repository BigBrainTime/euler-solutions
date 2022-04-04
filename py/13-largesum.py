import urllib.request

link = ("https://projecteuler.net/minimal=13")
raw = []

with urllib.request.urlopen(link) as url:
    data = url.readlines()

for i in range(2):
    data.pop(0)
data.pop()

for num in data:
    raw.append(int(str(num).replace("<br />\\n'", '').replace("b'","").replace("<br /></div>\\n'","")))

print(str(sum(raw))[0:10])