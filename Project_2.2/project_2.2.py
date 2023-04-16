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


def get_errors(a, b, x, algorythm, iter, error_):
    errors = np.array([x])
    for i in range(iter):
        x, error = algorythm(a, b, x)
        errors = np.concatenate((errors, np.array([error])), axis=0)
        if max(abs(error)) < error_:
            break

    return errors


class Sole:
    def __init__(self, algorythm=Seidel(), error=1e-3, iter=100):
        self.algorythm = algorythm
        self.error = error
        self.iter = iter

    def __call__(self, a, b):
        x = np.random.random(b.size) * 100
        errors = get_errors(a, b, x, self.algorythm, self.iter, self.error)
        errors_table = pd.DataFrame(errors, columns=["error x" + str(i) for i in range(b.size)])
        return f"Equation:\n{get_equation(a, b)}\n", f"Errors:\n{errors_table}\n\n", f"Result:\n{str(x)}"


A = np.array([
    [12, 0, 0, 3],
    [2, 20, -3, 0],
    [0, 2, 16, -1],
    [4, -2, 0, 24]
])
B = np.array([18, 39, -25, 0])


result = Sole()
# result = Sole(Jakobi())
for data in result(A, B):
    print(data)
