def modulo(a, b):
    """
    Функция для вычисления остатка от деления.
    :param a: делимое
    :param b: делитель
    :return: остаток от деления
    """
    if b == 0:
        raise ValueError("На ноль делить нельзя")
    return a % b

