import math

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def FMD():
    squares_list = list(i**2 for i in range(1, 102))
    primes_list = []
    for i in range(100):
        for j in range(squares_list[i] + 1, squares_list[i+1]):
            if is_prime(j):
                prime = j
                primes_list.append(prime)
                print(i, '(', squares_list[i], squares_list[i+1], '):', prime)
                break


def IYJ():
    primes = []
    for i in range(1000, 3170):
        num = i ** 2 + 1
        if num > 10000000:
            break
        if is_prime(num):
            primes.append(num)

    print(primes)
    print(len(primes))
    pass


def poly(x, c):
    return x**2 + x + c


def sweetness_factor(c, int_start, int_end):
    total_primes = 0
    total = 10000
    for x in range(int_start, int_end):
        val = poly(x, c)
        if val < 1:
            continue
        if is_prime(val):
            total_primes += 1

    return total_primes / total


def FJY():
    sweet = 0
    sweet_c = 0
    for c in range(-3999999, 4000001, 2):
        # keep a contant interval
        int_start = 0
        int_end = int_start + 10000
        sf = sweetness_factor(c, int_start, int_end)
        if sf > sweet:
            sweet = sf
            print(c, sf)
            sweet_c = c

    pass

FJY()
