"""
Function as taught in An Illustrated Theory of Numbers by Martin H. Weissman.
Function definition and more on the Euclidean Algorithm can be found in Chapter
1 on page 25.
LCM algorithm demonstrated on page 39.
"""
def get_GCD_euclidean_algorithm(a, b):
    while a % b != 0:
        c = a % b
        a = b
        b = c

    return c


def get_LCM_euclidean_algorithm(a, b):
    # LCM = a x b / gcd(a, b) (for positive a and b)
    # LCM(a, b) = LCM(|a|, |b|) thus we do not need to consider negative integers
    gcd = get_GCD_euclidean_algorithm(a, b)
    lcm = a * b / gcd
    return lcm


print(get_GCD_euclidean_algorithm(2059, 1711))
print(get_LCM_euclidean_algorithm(2059, 1711))
