# Fractal Generator 1.0

This program lets a user pick a known fractal set (such as the Mandelbrot set) and visualise it at a resolution they choose. The user can also click on an area that they'd like to zoom into, which re-renders the image; this can be done multiple times until the image loses clarity.

## How do I run this code?

First, clone the git repo to your machine by running the line
"git clone https://github.com/Tomm0Codes/sigma-capstone-project"
in your terminal.

Inside your working directory, create a venv by running the lines
"python3 -m venv .venv"
then
"source .venv/bin/activate"
in the terminal.

To install the required libraries for the code to run, enter the line
"pip install -r requirements.txt"

You can then run the file through your terminal with
"python3 mandelbrot.py"
then follow the instructions in the UI to generate your fractal. 