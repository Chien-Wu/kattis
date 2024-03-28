"https://open.kattis.com/problems/adolescentarchitecture"

import math

n = int(input(""))

blocks = []
for i in range(0, n):
    k = input("")
    blocks.append(k.split(" "))

for block in blocks:
    block[1] = int(block[1])

impossible = False
for block in blocks:
    if block[0] == "cube":
        l = int(block[1])
        for block in blocks:
            if block[0] == "cylinder" and l < int(block[1]) *2 < l * (math.sqrt(2)):
                impossible = True

for block in blocks:
    if block[0] == "cylinder":
        block[1] = block[1] * 1.8

blocks = sorted(blocks, key=lambda x: x[1])

for block in blocks:
    if block[0] == "cylinder":
        block[1] = int(block[1] / 1.8)

if impossible:
    print("impossible")
else:
    for block in blocks:
        print(block[0], block[1])
    




