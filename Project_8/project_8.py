def polynomial(coeffs, x):
    return sum([coeffs[len(coeffs) - i - 1] * pow(x, i) for i in range(len(coeffs))])


def intervaling(arg_a, arg_b, arg_eps, coeff):
    all_a, all_b = [arg_a], [arg_b]
    a, b = arg_a, arg_b
    k = 0
    len_internal = abs(a - b)
    all_x = [(a + b) / 2]

    while len_internal > arg_eps:
        mid = polynomial(coeff, all_x[-1])
        left_mid = a + len_internal / 4
        right_mid = b - len_internal / 4
        left_mid_f = polynomial(coeff, left_mid)
        right_mid_f = polynomial(coeff, right_mid)
        if left_mid_f < mid:
            all_a.append(all_a[-1])
            all_b.append(all_x[-1])
            b = all_x[-1]
            all_x.append(left_mid)
        elif right_mid_f < mid:
            all_a.append(all_x[-1])
            all_b.append(all_b[-1])
            a = all_x[-1]
            all_x.append(right_mid)
        else:
            all_a.append(left_mid)
            all_b.append(right_mid)
            a = left_mid
            b = right_mid
            all_x.append(all_x[-1])
        len_internal = abs(a - b)
        k += 1
    return all_x[-1], polynomial(coeff, all_x[-1]), k, all_x, all_a, all_b


def draw(k, all_x, all_a, all_b):
    result = "|" + f"{'-' * 123}" + "\n" + "|  {:2}  ".format(" k") + "|  {:^15}  ".format("Ak") + "|  {:^15}  ".format("Bk")
    result += "|  {:^15}  ".format("Xk(c)") + "|  {:^30}  ".format("L2k = [Ak; Bk]")
    result += "|  {:^15}  ".format("|L2k|") + "|\n|" + f"{'-' * 123}" + "\n"

    for i in range(k + 1):
        result += "|  {:2}  ".format(i) + "|  {:^15}  ".format(round(all_a[i], 3)) + "|  {:^15}  ".format(round(all_b[i], 3))
        result += "|  {:^15}  ".format(round(all_x[i], 3)) + "|  {:^30}  ".format(f"[{round(all_a[i], 3)}; {round(all_b[i], 3)}]")
        result += "|  {:^15}  ".format(round((all_b[i] - all_a[i]) / 2, 3)) + "|\n" + f"{'-' * 123}" + "\n"
    return result



interval = [0, 10]
eps = 0.01
# coeff = [1, -5, -10, 70]
coeff1 = int(input(f'Enter d1: '))
coeff2 = int(input(f'Enter d2: '))
coeff3 = int(input(f'Enter d3: '))
coeff4 = int(input(f'Enter d4: '))
str(input())
coeff = [coeff1, coeff2, coeff3, coeff4]

best_x, best_f, k_r, all_x_r, all_a_r, all_b_r = intervaling(interval[0], interval[1], eps, coeff)

print(f"Оптимальне значення х = {round(best_x, 4)}")
print(f"Мінімальне значення функції f(x) = {round(best_f, 4)}\n\n")
print(draw(k_r, all_x_r, all_a_r, all_b_r))
