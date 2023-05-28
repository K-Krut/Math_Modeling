import matplotlib.pyplot as plt
import numpy as np


def draw(x, y, name):
    """Function for drawing graphic"""
    plt.plot(x, y, 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(name)
    plt.grid(color='blue', linestyle='--', linewidth=0.5)
    plt.show()


# graphic 1
x_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_1 = np.array([4.409e-8, 4.517e-6, 6.168e-5, 3.682e-4, 1.392e-3, 3.931e-3, 9.034e-3, 1.779e-2, 3.108e-2, 4.928e-2])
name_1 = 'Pвідм = f(t)'
draw(x_1, y_1, name_1)

# graphic 2
x_2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_2 = np.array([0.2222222, 0.222221, 0.22221, 0.22214, 0.2219, 0.221, 0.22, 0.218, 0.215, 0.211])
name_2 = 'A = g(t)'
draw(x_2, y_2, name_2)

# graphic 3
x_3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y_3 = np.array([0.9999996, 0.999995, 0.99994, 0.9996, 0.999, 0.996, 0.991, 0.982, 0.969, 0.951])
name_3 = 'tоч = h(t)'
draw(x_3, y_3, name_3)
