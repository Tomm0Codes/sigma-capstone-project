import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def main():
    # Setup my  complex equations plot
    c_real_range = np.linspace(-2, 1, num=50)
    c_imag_range = np.linspace(-1.5, 1.5, num=50)
    real, imag = np.meshgrid(c_real_range, c_imag_range)
    c = real + imag*1j
    boundary = [
        c_real_range.min(), c_real_range.max(),
        c_imag_range.min(), c_imag_range.max()
    ]
    magnitude = np.abs(c)
    plt.imshow(magnitude, extent=boundary)
    plt.show()

    # If it converges, it's within the set, filled black,
    # else it's filled with colour based on the time taken to diverge


if __name__ == '__main__':
    main()
