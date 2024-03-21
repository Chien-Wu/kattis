"https://open.kattis.com/problems/almostperfect"
while True:
    number = int(input())

    divisor = []
    for i in range(1, number):
        if number % i == 0:
            divisor.append(i)
    if sum(divisor) == number:
        print(number, "perfect")
    elif sum(divisor) - number <= 2 and sum(divisor) - number >= -2:
        print(number, "almost perfect")
    else:
        print(number, "not perfect")

