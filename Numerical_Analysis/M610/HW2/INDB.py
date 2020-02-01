import numpy as np


def check_node_type(N, row, col):
    half = N // 2
    if row > half and col > half:
        return "outside of Omega"
    elif row == 0 or col == 0 or row == N or col == N or \
            (row == half and col >= half) or \
            (col == half and row >= half):
        return "boundary"
    else:
        return "interior"


def set_nodes(N):

    # Initialize counts and I matrix
    int_count = 0
    bound_count = 0
    I = np.zeros((N+1, N+1))
    J_i = np.array([])
    J_b = np.array([])

    for row_it in range(N+1):
        for col_it in range(N+1):
            node_type = check_node_type(N, row_it, col_it)

            if node_type == 'interior':
                int_count += 1
                I[row_it, col_it] = int_count

                # Fill J_i
                if int_count == 1:
                    J_i = np.hstack((J_i, np.array(([row_it, col_it]))))
                else:
                    J_i = np.vstack((J_i, np.array(([row_it, col_it]))))

            elif node_type == 'boundary':
                bound_count -= 1
                I[row_it, col_it] = bound_count

                # Fill J_b
                if bound_count == -1:
                    J_b = np.hstack((J_b, np.array(([row_it, col_it]))))
                else:
                    J_b = np.vstack((J_b, np.array(([row_it, col_it]))))

            else:
                # Assume that the node is outside of Omega
                I[row_it, col_it] = 0

    return I, J_i, J_b


# Set parameters
# N = 4
# I, J_i, J_b = set_nodes(N)
# print(I)
# print(J_i)
# print(J_b)




