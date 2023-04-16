import numpy as np


def get_matrix(arr):
    return '\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in arr])


def get_vector(arr):
    return f"({' '.join([f'{round(x, 2)}' for x in arr])})"


p_temp = np.array([])


def get_result(n, p, P):
    for i in range(n):
        global p_temp
        p_temp = p
        p = np.dot(p, P)
        print(f"{i + 1} крок")
        print(get_vector(p_temp) + " * matrix = " + get_vector(p))
        print(" ".join([f"p{j + 1}({i + 1}) = {np.round(p[j], 2)} " for j in range(len(p))]) + "\n")


iterations = 5
p_arr = np.array([1, 0, 0, 0, 0])
P_arr = np.array([[0.3, 0.2, 0.2, 0.15, 0.15],
                  [0, 0.40, 0.30, 0.20, 0.10],
                  [0, 0, 0.60, 0.30, 0.10],
                  [0, 0, 0, 0.45, 0.55],
                  [0, 0, 0, 0, 1]])

print(f"matrix = \n{get_matrix(P_arr)}\n\n")
get_result(iterations, p_arr, P_arr)