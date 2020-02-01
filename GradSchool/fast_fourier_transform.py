from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as plt


def run_fft(l):
    L = l
    n = 2**L
    h = 2 * np.pi / n
    j = np.arange(0, n, 1)

    # fj = 10 * np.cos(2 * j * h)
    # fj_fft = fft(fj)
    # fj_fft_real = np.real(fj_fft)
    # fj_ifft = ifft(fj_fft)
    # fj_ifft_real = np.real(fj_ifft)

    uj = 2*np.sin(2 * j * h) + np.cos(2 * j * h)
    uj_fft = fft(uj)
    uj_fft_real = np.real(uj_fft)
    uj_ifft = ifft(uj_fft)
    uj_ifft_real = np.real(uj_ifft)

    # Plot
    L = str(L)
    plt.plot(j, uj, label="Exact")
    plt.plot(j, uj_ifft_real, label="Approximate")
    plt.suptitle("FFT vs Exact for L = " + L)
    plt.title("$u_p = 2\sin(2t) - \cos(2t)$")
    plt.legend()

    plt.savefig("./Output/fft_L=" + L)

    plt.show()


for i in (3, 5, 8, 10):
    run_fft(i)
