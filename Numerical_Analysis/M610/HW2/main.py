import numpy as np
from Numerical_Analysis.M610.HW2.INDB import set_nodes


def TF_comp(J_i, f, h):
    """
    Computes and returns Tilde F.
    :param J_i: vector mapping node number to node indices for interior nodes
               (node number -> x_ij)
    :param f: right-hand side function f(x_1, x_2)
    :param h: mesh size
    :return: Tilde F, the vector of values of F on the interior nodes
    """
    TF = f(h*J_i[:, 0], h*J_i[:, 1])

    # Alternatively the above code can be written in a loop
    # for i in range(len(TF)):
    #     TF[i] = f(h * J_i[i, 0], h * J_i[i, 1])

    return TF


def AF_comp(Mi, I, Ji, a, b, g, TF, h):
    # Begin by computing A
    # Modify TF based on the boundary data
    pass


def f(x_1, x_2):
    return (1 + 8*np.pi**2) * np.sin(2*np.pi*x_1) * np.sin(2*np.pi*x_2)


def main():
    """
    Driver program for our Assignment.
    :return: The correct solution!
    """
    N = 4
    I, J_i, J_b = set_nodes(N)
    M_i = len(J_i)
    h = 1 / N
    TF = TF_comp(J_i, f, h)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
