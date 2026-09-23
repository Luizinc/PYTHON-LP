import os
import time
os.system('cls')

n = int(input('digite o numero: '))

for i in range(n, -1, -1):
    print(i)
    time.sleep(2)

print('fim')
