#In Progress
import RequestPull, textwrap

tri = RequestPull.pull(18)
high = 0
rows = []

for i in range(3):
    tem = str(tri[i])
    if len(tem) % 2 == 0:
        row = textwrap.wrap(tem, 2)
    else:
        row = textwrap.wrap(f"0{tem}", 2)
    rows.append(list(map(int, row)))

print(rows)