import numpy as np
import pandas as pd


class Seidel:
    def __call__(self, a, b, x):
        old_x = np.copy(x)
        for j in range(b.size):
            temp = b[j] - sum([a[j][i] * x[i] if j != i else 0 for i in range(b.size)])
            x[j] = temp / a[j][j]
        return x, old_x - x


class Jakobi:
    def __call__(self, a, b, x):
        old_x = np.copy(x)
        for j in range(b.size):
            temp = b[j] - sum([a[j][i] * old_x[i] if j != i else 0 for i in range(b.size)])
            x[j] = temp / a[j][j]
        return x, old_x - x


def get_equation(a, b):
    sole = ""
    for i in range(b.size):
        for j in range(b.size):
            sole += f" {str(a[i][j])}" + (f"x{str(j)} +" if j > 1 else "x + " if j == 1 else " +")
        sole = sole[:-1] + "= " + str(b[i]) + ";\n"
    return sole


def get_errors_(a, b, x, algorythm=Seidel(), iter=100, error_=1e-3):
    errors = np.array([x])
    for i in range(iter):
        x, error = algorythm(a, b, x)
        errors = np.concatenate((errors, np.array([error])), axis=0)
        if max(abs(error)) < error_:
            break

    return errors


class SOLE:
    def __init__(self, algorythm=Seidel(), error=1e-3, iterations=100):
        self.algorythm = algorythm
        self.error = error
        self.iterations = iterations

    def __call__(self, a, b):
        x = np.random.random(b.size) * 100
        print(get_equation(a, b))
        print(pd.DataFrame(get_errors_(a, b, x), columns=["error x" + str(i) for i in range(b.size)]))

        print("\nresult: " + str(x))

def get_errors(a, b, x, algorythm, iter, error_):
    errors = np.array([x])
    for i in range(iter):
        x, error = algorythm(a, b, x)
        errors = np.concatenate((errors, np.array([error])), axis=0)
        if max(abs(error)) < error_:
            break

    return errors
def sole(a, b, algorythm=Seidel(), iter=100, error_=1e-3):
    x = np.random.random(b.size) * 100
    print(get_equation(a, b))
    print(pd.DataFrame(get_errors(a, b, x, algorythm, iter, error_), columns=["error x" + str(i) for i in range(b.size)]))

    print("\nresult: " + str(x))


A = np.array([[36, 0, 4, -5], [2, 30, 0, -4], [4, 2, 32, 0], [0, 0, 11, 40]])
B = np.array([40, 39, -19, 31])
# task = SOLE(algorythm=Seidel())
# task = SOLE(algorythm=Jakobi())
#
# A = np.array([
#     [12, 0, 0, 3],
#     [2, 20, -3, 0],
#     [0, 2, 16, -1],
#     [4, -2, 0, 24]
# ])
# B = np.array([18, 39, -25, 0])
# task(A, B)
"""
 36 + 0x +  4x2 + -5x3 = 40;
 2 + 30x +  0x2 + -4x3 = 39;
 4 + 2x +  32x2 + 0x3 = -19;
 0 + 0x +  11x2 + 40x3 = 31;


"""


sole(A, B)