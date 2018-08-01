"""
Functions as taught in An Illustrated Theory of Numbers by Martin H. Weissman in
chapter 2 on Prime Factorization.
"""
import math

def prime_factor_decomposition(n):
    """
    The intent of this function is to find the prime factors of a given number n.
    :param n: value we wish to find the prime decomposition of
    :return: prime factors of n
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def main():
    # should be 2^2 3^1 5^2 7^1
    print(prime_factor_decomposition(111111))
    print(prime_factor_decomposition(math.factorial(10)))


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
