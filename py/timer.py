import time,os
from operator import itemgetter

auto = input('auto y/n:')
dir = os.listdir(os.path.join(os.getcwd(), 'py'))
if auto == 'n':
    print(dir)
while True and auto == 'n':
    file = input('Filename:')
    path=os.path.join(os.getcwd(),"py",file)
    start = time.time()
    os.system(f'python {path}')
    end=time.time()
    print(f'{round(end-start,2)} Seconds')
if auto=='n':
    quit()

for file in ('timer.py','test.py','__pycache__','RequestPull.py'):
    dir.remove(file)

files = []
for file in dir:
   files.append(file.split('-'))
for file in files:
    files[files.index(file)][0] = int(files[files.index(file)][0])
dir=[]
files = sorted(files,key=itemgetter(0))
for file in files:
    dir.append(f'{file[0]}-{file[1]}')
for file in dir:
    path = os.path.join(os.getcwd(), "py", file)
    print(path)
    start = time.time()
    os.system(f'python {path}')
    end = time.time()
    print(f'{round(end-start,2)} Seconds')