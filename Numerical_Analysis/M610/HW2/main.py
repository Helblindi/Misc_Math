import numpy as np
from Numerical_Analysis.M610.HW2.INDB import set_nodes
from scipy.sparse import bsr_matrix


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


def AF_comp(M_i, I, J_i, a, b, g, TF, h):
    # Begin by computing A
    A = bsr_matrix((M_i, M_i))
    print("testing:")
    print(A.toarray())
    vals = np.array([])
    m_indices = np.array([])
    m_indices = np.array([])
    # Iterate over J_i to find diagonal entries for A
    for i in range(M_i):
        pass
    # Modify TF based on the boundary data


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

    # placeholders
    a = 0
    b = 0
    g = 0
    AF_comp(M_i, I, J_i, a, b, g, TF, h)


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
