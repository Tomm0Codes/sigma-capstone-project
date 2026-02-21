import matplotlib.pyplot as plt
import numpy as np
import pyfiglet
from mpl_point_clicker import clicker
import sys


def main():
    user_fractal_type, user_resolution = fractal_UI()
    fractal_axes = {'Mandelbrot Set': (-2, 1, -1.5, 1.5)}
    fractal_gen_loop(
        user_fractal_type, user_resolution, *fractal_axes[user_fractal_type]
    )
    # TO-DO:
    # figure out way to go back a zoom step on keypress (main),
    # add new fractal options (long term)


def fractal_gen_loop(
    fractal_type: str,
    resolution: int,
    real_min: int,
    real_max: int,
    imag_min: int,
    imag_max: int,
):
    """
    Loop to open fractal figure, wait for user click,
    close figure, then open again on new zoomed point.
    """
    zoom = 5
    image_width = real_max - real_min
    image_height = imag_max - imag_min

    while True:
        fractal_generator(
            fractal_type, resolution, real_min, real_max, imag_min, imag_max
        )
        real_min = real_coord - (image_width / (2 * zoom))
        real_max = real_coord + (image_width / (2 * zoom))
        imag_min = imag_coord - (image_height / (2 * zoom))
        imag_max = imag_coord + (image_width / (2 * zoom))
        zoom *= zoom


def fractal_generator(
    fractal_type: str,
    resolution: int,
    real_min: int,
    real_max: int,
    imag_min: int,
    imag_max: int,
):
    """
    Generates a fractal image based on the axis range and resolution.
    """
    real, imag = np.meshgrid(
        np.linspace(real_min, real_max, num=resolution),
        np.linspace(imag_min, imag_max, num=resolution),
    )

    if fractal_type == 'Mandelbrot Set':
        c = real + imag * 1j
        vectorized_mandelbrot_func = np.vectorize(mandelbrot_func)
        boundary = [real_min, real_max, imag_min, imag_max]
        plt.imshow(
            vectorized_mandelbrot_func(c),
            interpolation=None,
            extent=boundary,
            origin='lower',
        )
        plt.connect('button_press_event', on_click)
        plt.connect('key_press_event', on_press)
        plt.show()
        # Add axis label


def on_press(event):
    """
    Closes my figure and program on keypress.
    """
    if event.key == 'x':
        sys.exit('Fractal Generator closed')
    elif event.key == 'b':
        ...


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
    of 0 if the number converges, or the count of how many iterations it takes
    for the initial number to diverge.
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
        try:
            user_input = int(input(s))
            if user_input in range(lower, upper + 1):
                return user_input

            print('Out of range, try again')

        except ValueError:
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
