import copy
import itertools
import matplotlib.pyplot as plt
import numpy as np


def get_coeff_denominator(copy_list, removed_element):
    """ Отримуємо дільник для інтерполяційного многочлена"""
    denominator = 1
    for j in range(len(copy_list)):
        denominator *= removed_element - copy_list[j]
    return denominator


def get_numerator_elements(combinations):
    """
    :param combinations: всі комбінації для перемноження
    :return: елементи чисельника
    """
    summ = 0
    for combination in combinations:
        mult = 1
        for elem in combination:
            mult *= -1 * elem
        summ += mult
    return summ


def coefficient(list_x, list_y):
    """
    :param list_x: значееня ряду xi
    :param list_y: значення ряду ƒ(xi)
    :return: коефіцієнти многочлена Лагранжа
    L3(x) = a*x^3 - b*x^2 + c*x + d => [a, b, c, d]
    L3(x) = 3/10*x^3 - 13/6*x^2 + 62/15*x + 1 => [0.3, -2.16667, 4.13333, 1]
    """
    if not (isinstance(list_x, list) or isinstance(list_y, list)):
        raise ValueError
    if len(list_x) != len(list_y) or len(list_x) < 2:
        raise ValueError

    list_coefficient = [0] * (len(list_x))

    # for i in range(1):
    for i in range(len(list_x)):
        removed_element = list_x[i]
        copy_list = copy.deepcopy(list_x)
        copy_list.pop(i)

        # дільник (x0 - x1)(x0 - x2)(x0 - x3)
        # (0 -2)(0 - 3)(0 - 5) = -30
        denominator = get_coeff_denominator(copy_list, removed_element)

        for j in range(0, len(copy_list) + 1):
            # комбінації для перемноження (x - x1)(x - x2)(x - x3)
            # (x - 2)(x - 3)(x - 5)
            combinations = list(itertools.combinations(copy_list, len(copy_list) - j))

            # ax^3 + bx^2 + cx + d (тут отримуємо a, b, c, d)
            # x^3 - 10x^2 + 31x - 30 (1, -10, 31, -30)
            summ = get_numerator_elements(combinations)

            # ділимо на знаменник всі значення чисельника многочлена
            # (x^3 - 10x^2 + 31x - 30) / -30
            summ /= denominator

            # множимо на значеня ƒ(xi), y0
            # (x - x1)(x - x2)(x - x3) / (x0 - x1)(x0 - x2)(x0 - x3) * y0
            summ *= list_y[i]
            list_coefficient[j] += summ
    return list_coefficient


def lagrange(x):
    """
    Розраховуємо значеня многочлена Лагранжа для якогось значення x
    :param x: аргумент х, для кого потрібно знайти значення
    """
    coefficients = coefficient(lagrange_x, lagrange_y)
    return sum([coefficients[i] * pow(x, i) for i in range(len(coefficients))])


def get_formula():
    """ Отримуємо формулу інтерполяційної функції y = Ln(x)"""
    coeffs = coefficient(lagrange_x, lagrange_y)
    formula = ""
    for i in range(len(coeffs)):
        formula = str(round(coeffs[i], 5)) + "x^" + str(i) + " " + formula
        if coeffs[i] > 0 and i != len(coeffs) - 1:
            formula = "+ " + formula
    return formula


def get_all_dots(*args):
    """
    Знаходиом значення L(xi) для ряду заданих точок
    :param args: xi
    :return: L(xi)
    """
    # знаходиом значення L(xi)
    for x in args:
        print("\nX= ", x, "\nY= ", round(lagrange(x), 5))


def draw():
    """Function for drawing graphic"""
    x = np.linspace(-10, 10, 100)
    y = lagrange(x)
    plt.plot(x, y, 'black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lagrange:')
    plt.grid(color='green', linestyle='--', linewidth=0.5)
    plt.show()

"""Коменарі для l0(x) з прикладу"""
lagrange_x = [-4, -3, 0, 1]
lagrange_y = [-7, 10, -11, -22]
print(get_formula())
get_all_dots(-2, -0.5, 0.5, 2)
draw()

"""Дані з прикладу в ДЗ"""
# lagrange_x = [0, 2, 3, 5]
# lagrange_y = [1, 3, 2, 5]
# print(get_formula())
# get_all_dots(4)
# draw()
