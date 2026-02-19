import matplotlib.pyplot as plt
import numpy as np
import pyfiglet
from mpl_point_clicker import clicker
import sys


def main():
    user_fractal_type, user_resolution = fractal_UI()
    fractal_axes = {'Mandelbrot Set': np.array(((-2, 1), (-1.5, 1.5)))}
    real_range, imag_range = fractal_axes[user_fractal_type]
    fractal_gen_loop(
        user_fractal_type, user_resolution, real_range, imag_range
    )


def fractal_gen_loop(
    fractal_type: str,
    resolution: int,
    real_range: np.ndarray,
    imag_range: np.ndarray,
):
    """
    Loop to open fractal figure, wait for user click,
    close figure, then open again on new zoomed point.
    """
    zoom = 1
    while True:
        fractal_generator(fractal_type, resolution, real_range, imag_range)
        zoom *= 10
        real_range = np.array(
            ((real_coord - 1 / zoom), (real_coord + 1 / zoom))
        )
        imag_range = np.array(
            ((imag_coord - 1 / zoom), (imag_coord + 1 / zoom))
        )


def fractal_generator(
    fractal_type: str,
    resolution: int,
    real_range: np.ndarray,
    imag_range: np.ndarray,
):
    """
    Generates a fractal image based on the axis range and resolution.
    """
    real, imag = np.meshgrid(
        np.linspace(real_range[0], real_range[1], num=resolution),
        np.linspace(imag_range[0], imag_range[1], num=resolution),
    )

    if fractal_type == 'Mandelbrot Set':
        c = real + imag * 1j
        vectorized_mandelbrot_func = np.vectorize(mandelbrot_func)
        mandelbrot_array = vectorized_mandelbrot_func(c)
        boundary = [real_range[0], real_range[1], imag_range[0], imag_range[1]]
        plt.imshow(mandelbrot_array, interpolation=None, extent=boundary)
        plt.connect('button_press_event', on_click)
        plt.connect('key_press_event', on_press)
        plt.show()


def on_press(event):
    """
    Closes my figure and program on keypress.
    """
    if event.key == 'x':
        sys.exit('Fractal Generator closed')


def on_click(event):
    """
    Accesses the coordinates of a click on the figure shown
    and closes the figure.
    """
    global real_coord, imag_coord
    if event.inaxes:
        plt.close()
        real_coord = event.xdata
        imag_coord = event.ydata


def mandelbrot_func(c: complex) -> int:
    """
    Takes a complex number and tests if it converges
    or diverges with repeated Mandelbrot iterations. It returns a count
    of 0 if the number converges, or the count for how long the number takes
    to diverge.
    """
    z = 0

    for iteration in range(250):
        z = z**2 + c
        # Escape radius is 2
        if abs(z) > 2:
            return iteration

        # TO-DO: add brent's cycle detection algorithm to
        # optimise converging points

    return 0


def user_integer_input(lower: int, upper: int, s: str) -> int:
    """
    This checks and returns the users integer input
    """
    while True:
        user_num = input(s)
        if user_num.isdigit() and int(user_num) in range(lower, upper + 1):
            return int(user_num)

        print('Invalid input, try again')


def fractal_UI() -> tuple:
    """
    Gives the user an interactive interface to choose
    a fractal and its resolution.
    """
    banner = pyfiglet.figlet_format('Fractal Generator 1.0', font='slant')
    print(banner)
    fractal_types = {
        1: 'Mandelbrot Set',
        # 2: 'Julia Sets',
        # 3: 'Newton Fractals'
    }

    for num, fractal_type in fractal_types.items():
        print(f'>>> {num}: {fractal_type}\n')

    fractal_type_choice = fractal_types[
        user_integer_input(
            1, len(fractal_types), 'Choose a fractal from the list above: '
        )
    ]
    resolution = user_integer_input(
        1, 1000, 'Enter a square resolution (1-1000): '
    )
    print('Click on the area you\'d like to zoom into, or press "x" to exit')
    return fractal_type_choice, resolution


if __name__ == '__main__':
    main()
