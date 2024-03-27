"https://open.kattis.com/problems/almostperfect"
import math

while True:
    try:
        number = int(input().strip())
    except EOFError:
        break
    
    divisor_sum = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisor_sum += i
            if i != number // i:
                divisor_sum += number // i
                    
    if divisor_sum == number:
        print(number, "perfect")
    elif abs(divisor_sum - number) <= 2:
        print(number, "almost perfect")
    else:
        print(number, "not perfect")

