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


def euler_cauchy(x0, xn, y0, h):
    n = (xn - x0) / h

    xi = x0  # x0 = 1.4
    yi = y0  # y0 = 2.2

    result = {'x': [], 'y': []}

    for i in range(int(n)):
        result['x'].append(round(xi, 4))  # записуємо результуюче значення xi
        result['y'].append(round(yi, 4))  # записуємо результуюче значення yi
        yi1_ = yi + h * f(xi, yi)  # ‾yi+1 = yi + hƒ(xi, yi)
        yi1 = yi + 0.5 * h * (f(xi, yi) + f(xi + h, yi1_))  # yi+1 = yi + h / 2 [ ƒ(xi, yi) + ƒ(xi+1, ‾yi+1) ]
        xi = xi + h  # перевизначаємо x | x = x + h
        yi = yi1  # перевизначаємо yi
    result['x'].append(round(xi, 4))  # записуємо результуюче значення xn
    result['y'].append(round(yi, 4))  # записуємо результуюче значення yn
    return result


def euler_enhanced(x0, xn, y0, h):
    n = (xn - x0) / h

    xi = x0  # x0 = 1.4
    yi = y0  # y0 = 2.2

    result = {'x': [], 'y': []}

    for i in range(int(n)):
        result['x'].append(round(xi, 4))  # записуємо результуюче значення xi
        result['y'].append(round(yi, 4))  # записуємо результуюче значення yi
        yi1 = yi + h * f(xi + h / 2, yi + h / 2 * f(xi, yi))  # yi+1 = yi + hƒ(xi + h / 2, yi + h / 2 ƒ(xi, yi))
        xi = xi + h  # перевизначаємо x | x = x + h
        yi = yi1  # перевизначаємо yi
    result['x'].append(round(xi, 4))  # записуємо результуюче значення xn
    result['y'].append(round(yi, 4))  # записуємо результуюче значення yn
    return result


def runge_kutte(x0, xn, y0, h):
    n = (xn - x0) / h

    xi = x0  # x0 = 1.4
    yi = y0  # y0 = 2.2

    result = {'x': [], 'y': []}

    for i in range(int(n)):
        result['x'].append(round(xi, 4))  # записуємо результуюче значення xi
        result['y'].append(round(yi, 4))  # записуємо результуюче значення yi
        k0 = f(xi, yi)
        k1 = f(xi + 0.5 * h, yi + 0.5 * h * k0)
        k2 = f(xi + 0.5 * h, yi + 0.5 * h * k1)
        k3 = f(xi + h, yi + h * k2)
        yi1 = yi + h / 6 * (k0 + 2 * k1 + 2 * k2 + k3)
        xi = xi + h  # перевизначаємо x | x = x + h
        yi = yi1  # перевизначаємо yi
    result['x'].append(round(xi, 4))  # записуємо результуюче значення xn
    result['y'].append(round(yi, 4))  # записуємо результуюче значення yn
    return result


def draw(data):
    """Function for drawing graphic"""
    x = np.linspace(1.4, 2.4, len(data))
    y = data
    plt.plot(x, y, 'green', label='y=sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(color='black', linestyle='--', linewidth=0.5)
    plt.legend(loc='best')
    plt.show()


def draw_all(euler_, euler_cauchy_, euler_enh, runge):
    """Function for drawing graphic"""
    x = np.linspace(1.4, 2.4, len(euler_))

    plt.plot(x, euler_, 'green', linewidth=0.2, label='Явний метод Ейлера')
    plt.plot(x, euler_cauchy_, 'black', linewidth=0.2, label='метод Ейлера-Коші')
    plt.plot(x, euler_enh, 'yellow', linewidth=0.2, label='Вдосконалений метод Ейлера')
    plt.plot(x, runge, 'red', linewidth=0.2, label='Рунге-Кутта')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(color='black', linestyle='--', linewidth=0.5)
    plt.legend(loc='best')
    plt.show()


def print_euler(data):
    for i in range(len(data['y'])):
        print(f'x{i}={data["x"][i]}; y{i}={data["y"][i]}')


def print_data_table(euler_, euler_cauchy_, euler_enhanced_, runge_kutte_):
    data = [euler_['x'], euler_['y'], euler_cauchy_['y'], euler_enhanced_['y'], runge_kutte_['y']]
    rows = [f'n = {x}' for x in range(len(data[0]))]
    data = np.transpose(data)
    columns = ('x', 'y Ейлер Явний', 'y Ейлера-Коші', 'y Ейлер Вд.', 'y Рунге-Кутта')
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
    cell_text = [[f'{x}' for x in data[row]] for row in range(len(data))]

    plt.box(on=None)

    plt.table(cellText=cell_text, rowLabels=rows,  rowColours=colors, colLabels=columns, loc='center')

    plt.xticks([])
    plt.yticks([])
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


x0_ = 1.4
xn_ = 2.4
y0_ = 2.2
h_ = 0.1

euler_data = euler(x0_, xn_, y0_, h_)
euler_cauchy_data = euler_cauchy(x0_, xn_, y0_, h_)
euler_enhanced_data = euler_enhanced(x0_, xn_, y0_, h_)
runge_kutte_data = runge_kutte(x0_, xn_, y0_, h_)

draw_all(euler_data['y'], euler_cauchy_data['y'], euler_enhanced_data['y'], runge_kutte_data['y'])
print_data_table(euler_data, euler_cauchy_data, euler_enhanced_data, runge_kutte_data)
