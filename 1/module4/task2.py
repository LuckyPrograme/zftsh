import time
from math import sqrt, factorial


def pi1(inter):
    start_time = time.time()
    pi = 2
    for i in range(1, inter):
        if i % 2 == 0:
            pi *= i / (i + 1)
        else:
            pi *= (i + 1) / i
    return f'pi={pi}, time={time.time() - start_time}'


def pi2(inter):
    start_time = time.time()
    pi = 90
    for i in range(1, inter):
        pi += i / (i ** 4)
    return f'pi={sqrt(sqrt(pi))}, time={time.time() - start_time}'


def pi3(inter):
    start_time = time.time()
    pi = 1
    n = 1
    for i in range(1, inter * 2, 2):
        n *= i/(i+1)
        if i % 4 == 1:
            pi -= (2 * i + 3) * (n ** 3)
        else:
            pi += (2 * i + 3) * (n ** 3)
    return f'pi={2/pi}, time={time.time() - start_time}'



def pi4(inter):
    start_time = time.time()
    pi = 1
    sq = sqrt(2)
    for i in range(1, inter):
        pi *= sq/2
        sq = sqrt(2+sq)
    return f'pi={2/pi}, time={time.time() - start_time}'



count_interactions = 10**7
print(pi1(count_interactions), pi2(count_interactions), pi3(count_interactions), pi4(count_interactions), sep='\n')
