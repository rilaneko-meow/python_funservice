import math
import re

def priority(op):
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 100

def lastOp(s):
    minPrt = 50
    k = -1
    for i, c in enumerate(s):
        if priority(c) <= minPrt:
            minPrt = priority(c)
            k = i
    return k

def Calc(s):
    s = s.strip()

    # Шаг 0: проверяем, является ли строка числом
    try:
        return float(s)
    except ValueError:
        pass  # если не число, продолжаем обработку

    # Шаг 1: добавляем недостающие скобки вокруг аргументов функций
    # Преобразуем sin1.2 → sin(1.2), sqrt9.0 → sqrt(9.0) и т. д.
    s = re.sub(r'(sin|cos|sqrt|abs)([0-9.]+)', r'\1(\2)', s)

    # Шаг 2: обрабатываем скобки
    while '(' in s and ')' in s:
        close_bracket = s.find(')')
        open_bracket = s.rfind('(', 0, close_bracket)
        if open_bracket == -1:
            raise SyntaxError("Несоответствие скобок")
        inner_expr = s[open_bracket + 1:close_bracket]
        inner_result = Calc(inner_expr)
        s = s[:open_bracket] + str(inner_result) + s[close_bracket + 1:]

    # Шаг 3: обрабатываем функции
    functions = ['abs', 'sin', 'cos', 'sqrt']
    for func in functions:
        pattern = rf'\\b{func}\\(([^()]*(?:\\([^()]*\\)[^()]*)*)\\)'
        match = re.search(pattern, s)
        while match:
            start, end = match.span()
            arg_expr = match.group(1)
            arg_result = Calc(arg_expr)  # рекурсивно вычисляем аргумент

            # Вычисляем значение функции
            if func == 'abs':
                func_result = abs(arg_result)
            elif func == 'sin':
                func_result = math.sin(arg_result)
            elif func == 'cos':
                func_result = math.cos(arg_result)
            elif func == 'sqrt':
                if arg_result < 0:
                    raise ValueError("Корень из отрицательного числа")
                func_result = math.sqrt(arg_result)

            # Заменяем вызов функции на результат
            s = s[:start] + str(func_result) + s[end:]
            match = re.search(pattern, s)  # ищем следующее вхождение

    # Шаг 4: ищем операции и вычисляем
    k = lastOp(s)
    if k < 0:  # если после всех преобразований строка — число
        return float(s)

    n1 = Calc(s[:k])
    n2 = Calc(s[k+1:])

    if s[k] == '+':
        return n1 + n2
    elif s[k] == '-':
        return n1 - n2
    elif s[k] == '*':
        return n1 * n2
    elif s[k] == '/':
        if n2 == 0:
            raise ZeroDivisionError("Деление на ноль")
        return n1 / n2
    else:
        raise ValueError(f"Неизвестная операция: {s[k]}")
