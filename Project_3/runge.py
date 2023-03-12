import math
import matplotlib.pyplot as plt
import numpy as np

"""
З точністю до 0.0001 знайти розв’язок задачі Коші для звичайного
диференційного рівняння першого порядку y' = y + cos(x / 13) на відрізку [1.4; 2.4] з
кроком h=0.1 за початкових умов y(1.4) = 2.2
"""


def f(x, y):
    return y + math.cos(x / 13)


def euler_cauchy(x0, xn, y0, h):
    n = (xn - x0) / h

    xi = x0  # x0 = 1.4
    yi = y0  # y0 = 2.2

    result = {'x': [], 'y': []}

    for i in range(int(n)):
        result['x'].append(round(xi, 4))                      # записуємо результуюче значення xi
        result['y'].append(round(yi, 4))                      # записуємо результуюче значення yi
        k0 = f(xi, yi)
        k1 = f(xi + 0.5 * h, yi + 0.5 * h * k0)
        k2 = f(xi + 0.5 * h, yi + 0.5 * h * k1)
        k3 = f(xi + h, yi + h * k2)
        yi1 = yi + h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
        xi = xi + h                                       # перевизначаємо x | x = x + h
        yi = yi1                                          # перевизначаємо yi
    result['x'].append(round(xi, 4))                          # записуємо результуюче значення xn
    result['y'].append(round(yi, 4))                          # записуємо результуюче значення yn
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


"""

def draw(data, data2):
    x = np.linspace(1.4, 2.4, len(data))
    y = data
    x2 = np.linspace(1.4, 2.4, len(data))
    y2 = data2
    plt.plot(x, y, 'black', label='cauchy-euler')
    plt.plot(x2, y2, 'green')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.show()

"""

#                  x0    xn   y0   h
euler_data = euler_cauchy(1.4, 2.4, 2.2, 0.1)
print_euler(euler_data)
draw(euler_data['y'])
