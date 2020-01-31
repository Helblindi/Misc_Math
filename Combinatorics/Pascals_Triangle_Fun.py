import numpy as np
import math


def numOnes(n):
    if n == 0 or n == 1:
        return 1

    k = math.floor(math.log(n, 2))
    return k * numOnes(n - 2 ** k)


def main():
    result = numOnes(4)
    print(result)


if __name__ == '__main__':
    main()