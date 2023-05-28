import numpy as np
from math import factorial


def get_probabilities_m(ro, n, m):
    return np.array([ro ** i / factorial(i) for i in range(n + 1)] + [ro ** (n + i) / n ** i / factorial(n) for i in
                                                                      range(1, m + 1)])


def get_probabilities(ro, n):
    return np.array([1 / (np.sum([ro ** i / factorial(i) for i in range(n + 1)])
                          + ro ** (n + 1) / factorial(n) / (n - ro))])


def get_r_m(ro, prob, n, m, gamma):
    return (ro ** (n + 1) * prob[0] / n / factorial(n) * (1 - (m + 1) * gamma ** m + m * gamma ** (m + 1)) /
            (1 - gamma) ** 2)


def get_r(ro, prob, n, gamma):
    return ro ** (n + 1) * prob[0] / n / factorial(n) / (1 - gamma) ** 2


def queueing_systems(ar, dr, n, m=-1):
    if n < 1:
        raise ValueError('каналів має бути більше 1 ')

    ro = ar / dr
    gamma = ro / n

    if m > -1:
        # prob = probabilities
        prob = get_probabilities_m(ro, n, m)
        prob[0] = 1 / np.sum(prob)
        prob[1:] *= prob[0]
        P_failure = prob[-1]
        r = get_r_m(ro, prob, n, m, gamma)
    else:
        prob = get_probabilities(ro, n)
        P_failure = 0

        r = get_r(ro, prob, n, gamma)

    Q = 1 - P_failure
    A = Q * ar

    z = A / dr

    k = z + r

    t_och = r / ar
    t_sys = Q / dr + t_och

    return {
        'Інтенсивність вхідного потоку λ': ar,
        'Інтенсивність потоку обслуговування μ': dr,
        'Канали n': n,
        'Число місць в черзі m': m,

        '-----------------': '-----------------',

        'Приведена інтенсивність ρ': ro,

        '------------------': '-----------------',

        'Граничні ймовірності': prob,
        'Сума граничних ймовірностей': np.sum(prob),

        '-------------------': '-----------------',

        'Імовірність відмови в обслуговуванні Pвідм': P_failure,
        'Відносна пропускна здатність Q': Q,
        'Абсолютна пропускна здатність A': A,

        '--------------------': '-----------------',

        'Середня кількість зайнятих каналів z': z,
        'Середня кількість заявок в черзі r': r,
        'Середня кількість заявок, пов’язаних із системою k': k,

        '---------------------': '-----------------',

        'Середній час очікування заявки в черзі (хвилин) tоч': t_och,
        'Середній час перебування заявки в системі (хвилин) tсист': t_sys
    }


def print_result(result):
    for key, val in result.items():
        if isinstance(val, float):
            print(f"{key} = {val:.3f}")
        elif isinstance(val, np.ndarray):
            val_str = "\n\t".join(list(map(lambda x: f"p{x[0]} - {x[1]:.3f}", enumerate(val))))
            print(f'{key}:\n\t{val_str}')
        else:
            print(f"{key} = {val}")


def proces():
    while True:
        try:
            channels = int(input('канали: '))
            queue = int(input('число місць в черзі (якщо необмежена: -1): '))
            arrival_rates = float(input('інтенсивність вхідного потоку: '))
            departure_rates = float(input('інтенсивність потоку обслуговування: '))
            print_result(queueing_systems(arrival_rates, departure_rates, channels, queue))
        except Exception as e:
            print(e)
        if input("Enter 0 to exit, else to continue\n") == '0':
            break


proces()
