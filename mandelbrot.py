"""Fractal Generator, currently including the Mandelbrot Set"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import pyfiglet


def main():
    """Full Generator function"""
    user_fractal_type, user_resolution = fractal_user_interface()
    fractal_axes_options = {'Mandelbrot Set': [-2, 1, -1.5, 1.5]}
    fractal_gen_loop(
        user_fractal_type, user_resolution,
        fractal_axes_options[user_fractal_type]
    )
    # TO-DO:
    # figure out way to go back a zoom step on keypress (main),
    # add user option for different colour mapping
    # add new fractal options (long term)


def fractal_gen_loop(
    fractal_type: str,
    resolution: int,
    fractal_axes: tuple
):
    """Loop to open fractal figure, wait for user click,
    close figure, then open again on new zoomed point.
    """
    zoom = 5
    image_width = fractal_axes[1] - fractal_axes[0]
    image_height = fractal_axes[3] - fractal_axes[2]

    while True:
        fractal_generator(
            fractal_type, resolution, fractal_axes
        )
        image_width = fractal_axes[1] - fractal_axes[0]
        image_height = fractal_axes[3] - fractal_axes[2]
        fractal_axes[0] = real_coord - (image_width / (2 * zoom))
        fractal_axes[1] = real_coord + (image_width / (2 * zoom))
        fractal_axes[2] = imag_coord - (image_height / (2 * zoom))
        fractal_axes[3] = imag_coord + (image_width / (2 * zoom))
        zoom *= zoom


def fractal_generator(
    fractal_type: str,
    resolution: int,
    fractal_axes: tuple
):
    """Generates a fractal image based on the axis range and resolution.
    """
    real, imag = np.meshgrid(
        np.linspace(fractal_axes[0], fractal_axes[1], num=resolution),
        np.linspace(fractal_axes[2], fractal_axes[3], num=resolution),
    )

    if fractal_type == 'Mandelbrot Set':
        c = real + imag * 1j
        vectorized_mandelbrot_func = np.vectorize(mandelbrot_func)
        boundary = fractal_axes
        vectorized_mandelbrot = vectorized_mandelbrot_func(c)
        masked_array = np.ma.masked_where(
            vectorized_mandelbrot == 0, vectorized_mandelbrot
        )
        plt.imshow(
            masked_array,
            interpolation=None,
            extent=boundary,
            origin='lower',
        )
        plt.title('Mandelbrot Set')
        plt.xlabel('Re(c)')
        plt.ylabel('Im(c)')
        plt.colorbar().ax.set_title('#Iterations to Diverge')
        plt.connect('button_press_event', on_click)
        plt.connect('key_press_event', on_press)
        plt.gca().set_facecolor('black')
        plt.show()


def on_press(event):
    """Closes my figure and program on keypress.
    """
    if event.key == 'x':
        sys.exit('Fractal Generator closed')
    elif event.key == 'b':
        ...


def on_click(event):
    """Accesses the coordinates of a click on the figure shown
    and closes the figure.
    """
    global real_coord, imag_coord
    if event.inaxes:
        plt.close()
        real_coord = event.xdata
        imag_coord = event.ydata


def mandelbrot_func(c: complex) -> int:
    """Takes a complex number and tests if it converges
    or diverges with repeated Mandelbrot iterations. It returns a count
    of 0 if the number converges, or the count of how many iterations it takes
    for the initial number to diverge.
    """
    z = 0

    for iteration in range(1, 251):
        z = z**2 + c
        # Escape radius is 2
        if abs(z) > 2:
            return iteration

        # TO-DO: add brent's cycle detection algorithm to
        # optimise converging points

    return 0


def user_integer_input(lower: int, upper: int, s: str) -> int:
    """This checks and returns the users integer input
    """
    while True:
        try:
            user_input = int(input(s))
            if user_input in range(lower, upper + 1):
                return user_input

            print('Out of range, try again')

        except ValueError:
            print('Invalid input, try again')


def fractal_user_interface() -> tuple:
    """Gives the user an interactive interface to choose
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
