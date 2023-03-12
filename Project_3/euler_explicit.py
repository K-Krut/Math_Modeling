import math
import matplotlib.pyplot as plt
import numpy as np

"""
З точністю до 0.0001 знайти розв’язок задачі Коші для звичайного
диференційного рівняння першого порядку y' = y + cos(x / 13) на відрізку [1.4; 2.4] з
кроком h=0.1 за початкових умов y(1.4) = 2.2
"""

# Define the function f(x, y) = y + cos(x/13)
def f(x, y):
    return y + math.cos(x / 13)


def euler(x0, xn, y0, h):
    n = (xn - x0) / h

    yi = y0
    xi = x0

    res = []
    for i in range(int(n)):
        res.append(round(yi, 4))
        print(f'x{i} = {round(xi, 4)}; y{n} = {round(yi, 4)}')
        xi = xi + h
        yi = yi + h * f(xi, yi)
    print(f'x{n} = {round(xi, 4)}; y{n} = {round(yi, 4)}')
    return res


def draw(data):
    """Function for drawing graphic"""
    x = np.linspace(1.4, 2.4, 10)
    y = data
    plt.plot(x, y, 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.show()
    """
    fig, ax = plt.subplots(figsize=(12,8))
    plt.plot(x, y)
    plt.xlabel("x values", size=12)
    plt.ylabel("y values", size=12)
    plt.title("Learning more about pyplot with random numbers chart", size=15)
    for index in range(len(x)):
      ax.text(x[index], y[index], y[index], size=12)
    plt.xticks(x, size=12)
    plt.yticks([i for i in range(20)], size=12)
    plt.grid()
    plt.show()
    """

#                  x0    xn   y0   h
euler_data = euler(1.4, 2.4, 2.2, 0.1)
draw(euler_data)

# # Define the initial conditions
# x0 = 1.4
# y0 = 2.5
# h = 0.1
# accuracy = 0.0001
#
# # Set up the loop to iterate over the interval [1.4, 2.4]
# x = x0
# y = y0
# while x <= 2.4:
#     # Calculate the next value of y using the Euler method formula
#     y_next = y + h * f(x, y)
#
#     # Check if the difference between the calculated and true solution is less than the desired accuracy
#     if abs(y_next - (2.5 * math.exp(x - 1.4) - math.sin(x / 13))) < accuracy:
#         break
#
#     # Update the values of x and y
#     x += h
#     y = y_next
#
# # Output the result
# print("The solution at x = 2.4 is:", y)
