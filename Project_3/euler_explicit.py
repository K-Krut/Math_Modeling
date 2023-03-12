import math
import matplotlib.pyplot as plt
import numpy as np

"""
З точністю до 0.0001 знайти розв’язок задачі Коші для звичайного
диференційного рівняння першого порядку y' = y + cos(x / 13) на відрізку [1.4; 2.4] з
кроком h=0.1 за початкових умов y(1.4) = 2.2
"""


def f(x, y):
    """ f(x, y) = y + cos(x/13) """
    return y + math.cos(x / 13)


def euler(x0, xn, y0, h):
    n = (xn - x0) / h

    x = x0
    y = y0

    result = {'x': [], 'y': []}
    for i in range(int(n)):
        result['x'].append(round(x, 4))
        result['y'].append(round(y, 4))
        x = x + h
        y = y + h * f(x, y)
    result['x'].append(round(x, 4))
    result['y'].append(round(y, 4))
    return result


def print_euler(data):
    for i in range(len(data['y'])):
        print(f'x{i}={data["x"][i]}; y{i}={data["y"][i]}')


def draw(data):
    """Function for drawing graphic"""
    x = np.linspace(1.4, 2.4, len(data))
    y = data
    plt.plot(x, y, 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.show()


#                  x0    xn   y0   h
euler_data = euler(1.4, 2.4, 2.2, 0.1)
print_euler(euler_data)
draw(euler_data['y'])
