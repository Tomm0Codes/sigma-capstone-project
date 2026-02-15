import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def main():
    # Setup a "fractal generator UI"
    # Get resolution from user
    # Get type of fractal from user from pre list or one they want to try out

    # Find a way to turn it into an animation that keeps the quality as you zoom in
    # Setup my  complex equations plot
    # If it converges, it's within the set - no colour,
    # else it's filled with colour based on the time taken to diverge
    resolution = resolution_input()
    c_real_range = np.linspace(-2, 1, num=1000)
    c_imag_range = np.linspace(-1.5, 1.5, num=1000)
    real, imag = np.meshgrid(c_real_range, c_imag_range)
    boundary = [
        c_real_range.min(), c_real_range.max(),
        c_imag_range.min(), c_imag_range.max()
    ]
    c = real + imag*1j
    vectorized_divergence_test = np.vectorize(divergence_test)
    plt.imshow(
        vectorized_divergence_test(c),
        interpolation=None,
        extent=boundary
    )
    plt.show()


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
    while count < 25:
        z = z**2 + c
        count += 1

        # Escape radius is 2
        if abs(z) >= 2:
            return count

    return 0


def resolution_input() -> int:
    '''
    This takes the users integer input between 0-300 for the DPI
    resolution
    '''
    while True:
        resolution = input('Enter a DPI resolution between 0-300: ')
        if resolution.isdigit() and int(resolution) in range(1, 301):
            return int(resolution)

        print('Invalid input, try again')


if __name__ == '__main__':
    resolution = resolution_input()
    print(resolution)
