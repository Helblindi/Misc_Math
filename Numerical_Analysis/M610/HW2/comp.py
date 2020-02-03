import numpy as np
from scipy.sparse import csr_matrix


def TF_comp(J_i, f, h):
    """
    Computes and returns Tilde F.
    :param J_i: vector mapping node number to node indices for interior nodes
               (node number -> x_ij)
    :param f: right-hand side function f(x_1, x_2)
    :param h: mesh size
    :return: Tilde F, the vector of values of F on the interior nodes
    """
    TF = f([h * J_i[:, 0], h * J_i[:, 1]])

    # Alternatively the above code can be written in a loop
    # for i in range(len(TF)):
    #     TF[i] = f(h * J_i[i, 0], h * J_i[i, 1])

    return TF


def AF_comp(M_i, I, J_i, a, b, g, TF, h):
    # Begin by computing A
    vals = np.array([])
    m_indices = np.array([])
    n_indices = np.array([])

    # Iterate over J_i to find diagonal entries for A
    for l in range(M_i):
        # compute the diagonal entry
        l_m, l_n = J_i[l]
        val = (a([l_m - 1, l_n]) + a([l_m + 1, l_n]) + b([l_m, l_n - 1]) + b([l_m, l_n + 1])) / h ** 2

        # Append this val to the vals array to be put into the sparse matrix A
        vals = np.append(vals, val)
        m_indices = np.append(m_indices, l)
        n_indices = np.append(n_indices, l)

        # Determine what to do with the neighboring nodes
        # order to iterate is left, right, down, up
        directions = ["left", "right", "down", "up"]
        neighboring_nodes = [[l_m - 1, l_n], [l_m + 1, l_n], [l_m, l_n - 1], [l_m, l_n + 1]]
        for it in range(4):
            node = neighboring_nodes[it]
            direction = directions[it]
            m = int(node[0])
            n = int(node[1])
            indicator = I[m, n]
            assert indicator != 0
            if indicator > 0:
                # this means we have an internal node
                ex_val = 0
                if direction == "left" or direction == "right":
                    ex_val = a([m, n]) / h ** 2
                elif direction == "down" or direction == "up":
                    ex_val = b([m, n]) / h ** 2
                else:
                    print("PROBLEM with direction.")

                # Append to the respective arrays the value and index to go in the sparse matrix
                vals = np.append(vals, ex_val)
                m_indices = np.append(m_indices, l)
                n_indices = np.append(n_indices, indicator - 1)

            else:
                # this means we are dealing with a boundary node
                # Append the known value to the TF vector, ultimately forming F
                TF[l] += g([m, n])

    # Create sparse matrix A.  See documentation at the following reference:
    # https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.sparse.csr_matrix.html
    A = csr_matrix((vals, (m_indices, n_indices)), shape=(M_i, M_i))
    F = TF

    return A, F
