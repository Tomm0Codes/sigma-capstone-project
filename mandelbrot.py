import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def main():
    # Setup my  complex equations plot
    c_real_range = np.linspace(-2, 1, num=50)
    c_imag_range = np.linspace(-1.5, 1.5, num=50)
    real, imag = np.meshgrid(c_real_range, c_imag_range)
    c_range = real + imag*1j
    boundary = [
        c_real_range.min(), c_real_range.max(),
        c_imag_range.min(), c_imag_range.max()
    ]
    magnitude = np.abs(c_range)
    plt.imshow(magnitude, extent=boundary)
    plt.show()
    # If it converges, it's within the set - no colour,
    # else it's filled with colour based on the time taken to diverge
    divergence_time = divergence_test(c_range)


def divergence_test(c_array: np.ndarray) -> np.ndarray:
    '''
    This function takes the meshgrid of complex numbers and returns
    0 if, in the Mandelbrot set formula, the number converges,
    else the approximate time required for the number to diverge.

    :param c: Array of test values for c
    :type c: np.ndarray
    :return: Array of time taken to converge/diverge
    :rtype: ndarray[_AnyShape, dtype[Any]]
    '''
    z = np.array([0])


if __name__ == '__main__':
    main()
