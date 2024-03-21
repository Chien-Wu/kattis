"https://open.kattis.com/problems/3dprinter"

n = int(input())

printer = 1
status = 0
day = 0

while  status < n:
    if n > 2 * printer:
        printer = printer * 2
    else:
        status += printer
    day = day+1
print(day)