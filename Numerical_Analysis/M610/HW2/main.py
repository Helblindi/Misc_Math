import numpy as np
from scipy.sparse.linalg import spsolve
from Numerical_Analysis.M610.HW2.INDB import set_nodes
from Numerical_Analysis.M610.HW2.comp import TF_comp, AF_comp


def f2(x):
    return (1 + 8*np.pi**2) * np.sin(2*np.pi*x[0]) * np.sin(2*np.pi*x[1])


def a2(x):
    return 1


def b2(x):
    return 1


def g2(x):
    return 0


def u2(x):
    """ Gives true solution for problem 2. """
    return np.sin(2*np.pi*x[0])*np.sin(2*np.pi*x[1])


def problem_2():
    N_vals = [8, 16, 32, 64, 128]
    max_errors = np.array([])
    for N in N_vals:
        # Step 1: Compute arrays
        I, J_i, J_b = set_nodes(N)

        # Set a few variables that will be used later
        M_i = len(J_i)
        h = 1 / N

        # Step 2:  Set the right hand side vector TF by calling TFcomp.
        TF = TF_comp(J_i, f2, h)

        # Step 3: Generate the sparse matrix A and F by calling AFcomp.
        A, F = AF_comp(M_i, I, J_i, a2, b2, g2, TF, h)

        # Step 4: Compute the approximate solution U=A\F.
        # http://pageperso.lif.univ-mrs.fr/~francois.denis/IAAM1/scipy-html-1.0.0/generated/scipy.sparse.linalg.spsolve.html
        U = spsolve(A, F)

        # Step 5: Compute and report the errors.
        errors = np.array([])
        for l in range(M_i):
            solution = u2(J_i[l])
            error = np.abs(U[l] - solution)
            errors = np.append(errors, error)
        print("Max error for N = %d: %f." % (N, np.max(errors)))
        max_errors = np.append(max_errors, np.max(errors))

    # Step 6: Get an estimate for the rate of convergence.
    conv_rates = np.array([])
    for i in range(1, len(max_errors)):
        conv_rate = np.log(max_errors[i-1]/max_errors[i])/np.log(2)
        conv_rates = np.append(conv_rates, conv_rate)
        print("Convergence rate for N = %d: %f." % (N_vals[i], conv_rate))


def f3(x):
    return -6 - 4*x[0] + 4*x[1]


def a3(x):
    return 1 + x[0]


def b3(x):
    return 2 - x[1]


def g3(x):
    return u3(x)


def u3(x):
    """ Gives true solution for problem 3. """
    return x[0]**2 + x[1]**2


def problem_3():
    N_vals = [8, 16, 32, 64, 128]
    max_errors = np.array([])
    for N in N_vals:
        # Step 1: Compute arrays
        I, J_i, J_b = set_nodes(N)

        # Set a few variables that will be used later
        M_i = len(J_i)
        h = 1 / N

        # Step 2:  Set the right hand side vector TF by calling TFcomp.
        TF = TF_comp(J_i, f3, h)

        # Step 3: Generate the sparse matrix A and F by calling AFcomp.
        A, F = AF_comp(M_i, I, J_i, a3, b3, g3, TF, h)

        # Step 4: Compute the approximate solution U=A\F.
        # http://pageperso.lif.univ-mrs.fr/~francois.denis/IAAM1/scipy-html-1.0.0/generated/scipy.sparse.linalg.spsolve.html
        U = spsolve(A, F)

        # Step 5: Compute and report the errors.
        errors = np.array([])
        for l in range(M_i):
            solution = u3(J_i[l])
            error = np.abs(U[l] - solution)
            errors = np.append(errors, error)
        print("Max error for N = %d: %f." % (N, np.max(errors)))
        max_errors = np.append(max_errors, np.max(errors))


def main():
    """
    Driver program for our Assignment.
    :return: The correct solution!
    """
    problem_2()
    problem_3()


# While not required, it is considered good practice to have
# a main function and use this syntax to call it.
if __name__ == "__main__":
    main()
