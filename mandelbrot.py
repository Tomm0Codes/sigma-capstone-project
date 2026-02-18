import matplotlib.pyplot as plt
import numpy as np
import pyfiglet
from mpl_point_clicker import clicker


def main():
    # Setup a "fractal generator UI" that gets choice of visual
    # (optional) and resolution for image
    resolution, fractal_type_choice = fractal_UI()
    fractal_generator(resolution, fractal_type_choice)

    # Find a way to turn it into an animation that keeps the quality as you zoom in (main goal)


def fractal_generator(fractal_type: str, resolution: int):
    c_real_range = np.linspace(-0.8, -0.7, num=resolution)
    c_imag_range = np.linspace(0.05, 0.15, num=resolution)
    real, imag = np.meshgrid(c_real_range, c_imag_range)
    boundary = [
        c_real_range.min(), c_real_range.max(),
        c_imag_range.min(), c_imag_range.max()
    ]
    c = real + imag*1j
    vectorized_mandelbrot_func = np.vectorize(mandelbrot_func)
    plt.imshow(
        vectorized_mandelbrot_func(c),
        interpolation=None,
        extent=boundary
    )
    plt.connect('button_press_event', on_click)
    plt.show()
    print(real_coord, imag_coord)


def on_click(event) -> tuple:
    '''
    Accesses the coordinates of a click on the figure shown
    and closes the figure
    '''
    global real_coord, imag_coord
    if event.inaxes:
        plt.close()
        real_coord = event.xdata
        imag_coord = event.ydata


def mandelbrot_func(c: complex) -> int:
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
    while count < 250:
        z = z**2 + c
        count += 1

        # Escape radius is 2
        if abs(z) >= 2:
            return count

    return 0


def user_integer_input(lower: int, upper: int, s: str) -> int:
    '''
    This checks and returns the users integer input
    '''
    while True:
        user_num = input(s)
        if user_num.isdigit() and int(user_num) in range(lower, upper+1):
            return int(user_num)

        print('Invalid input, try again')


def fractal_UI() -> tuple:
    '''
    This function gives the user an interactive interface to choose
    a fractal (or make their own) and its resolution.
    '''
    banner = pyfiglet.figlet_format(
        'Fractal Generator 1.0',
        font='slant'
    )
    print(banner)
    fractal_types = {
        1: 'Mandelbrot Fractals',
        2: 'Julia Sets',
        3: 'Newton Fractals'
    }

    for num, fractal_type in fractal_types.items():
        print(f'>>> {num}: {fractal_type}\n')

    fractal_type_choice = user_integer_input(
        1,
        len(fractal_types),
        'Choose a fractal from the list above: '
    )
    resolution = user_integer_input(
        1,
        1000,
        'Enter a square resolution (1-1000): '
    )
    return fractal_type_choice, resolution


if __name__ == '__main__':
    main()
