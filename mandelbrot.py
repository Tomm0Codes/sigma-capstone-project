import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def main():
    # Setup my  complex equations plot
    c_real_range = np.linspace(-2, 1, num=50)
    c_imag_range = np.linspace(-1.5, 1.5, num=50)
    real, imag = np.meshgrid(c_real_range, c_imag_range)
    boundary = [
        c_real_range.min(), c_real_range.max(),
        c_imag_range.min(), c_imag_range.max()
    ]
    c = real + imag*1j
    # look into applying function to whole array of c values

    # plt.imshow(, extent=boundary)
    # plt.show()

    # If it converges, it's within the set - no colour,
    # else it's filled with colour based on the time taken to diverge


def divergence_test(c: complex) -> int:
    '''
    This function takes a complex number and tests if it converges
    or diverges with repeated Mandelbrot iterations. It returns a count
    of 0 if the number converges, or the count for how long the number takes
    to diverge.

    :param c: Complex number to test
    :return: Iterations taken to converge/diverge
    '''
    z = 0
    count = 0
    while count < 20:
        z = z**2 + c
        print(z)
        count += 1

        # Escape radius is 2
        if abs(z) >= 2:
            return count

    return 0


if __name__ == '__main__':
    print(divergence_test(1j))
