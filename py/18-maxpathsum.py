#In Progress
import RequestPull, textwrap

tri = RequestPull.pull(18)
high = 0

for i in range(len(tri)):
    tem = str(tri[i])
    if len(tem) % 2 == 0:
        globals()[f"row{i}"] = textwrap.wrap(tem, 2)
    else:
        globals()[f"row{i}"] = textwrap.wrap(f"0{tem}", 2)
    globals()[f"row{i}"] = list(map(int, globals()[f"row{i}"]))

    

print(high)