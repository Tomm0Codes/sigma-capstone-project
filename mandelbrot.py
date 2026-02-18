import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pyfiglet


def main():
    pass
    # Setup a "fractal generator UI" that gets choice of visual
    # (optional) and resolution for image
    # Find a way to turn it into an animation that keeps the quality as you zoom in (main goal)


def draw_me(img: np.ndarray):
    ...


def fractal_generator():
    c_real_range = np.linspace(-2, 1, num=1000)
    c_imag_range = np.linspace(-1.5, 1.5, num=1000)
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
    plt.show()


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
    while count < 25:
        z = z**2 + c
        count += 1

        # Escape radius is 2
        if abs(z) >= 2:
            return count

    return 0


def user_integer_input(min: int, max: int, num_info: str) -> int:
    '''
    This checks and returns the users integer input
    '''
    while True:
        user_num = input(f'{num_info} from {min}-{max}: ')
        if user_num.isdigit() and int(user_num) in range(min, max):
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
    fractals = {
        1: 'Mandelbrot Fractals',
        2: 'Julia Sets',
        3: 'Newton Fractals'
    }
    fractal_choice = user_integer_input(1, 3, 'Choose a fractal')
    resolution = user_integer_input(1, 300, 'Enter a DPI resolution')


if __name__ == '__main__':
    main()
