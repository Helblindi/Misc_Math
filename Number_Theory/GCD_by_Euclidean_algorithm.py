"""
Function as taught in An Illustrated Theory of Numbers by Martin H. Weissman.
Function definition and more on the Euclidean Algorithm can be found in Chapter
1 on page 25.
"""
def get_GCD_euclidean_algorithm(a, b):
    while a % b != 0:
        c = a % b
        a = b
        b = c

    return c


print(get_GCD_euclidean_algorithm(2059, 1711))
