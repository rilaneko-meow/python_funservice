import math

def find_matching_bracket(s, start):
    bracket_count = 1
    for i in range(start + 1, len(s)):
        if s[i] == '(':
            bracket_count += 1
        elif s[i] == ')':
            bracket_count -= 1
            if bracket_count == 0:
                return i
    return -1  # не найдена закрывающая скобка

def Calc(s):
    s = s.strip()

    # Шаг 1: обрабатываем функции (sin, cos, sqrt, abs)
    functions = ['sin', 'cos', 'sqrt', 'abs']
    for func in functions:
        while func + '(' in s:
            # Находим позицию начала функции
            start = s.find(func + '(')
            # Находим соответствующую закрывающую скобку
            end = find_matching_bracket(s, start)
            if end == -1:
                raise SyntaxError(f"Незакрытая скобка для функции {func}")
            # Извлекаем аргумент функции
            arg_str = s[start + len(func) + 1:end]
            arg = Calc(arg_str)  # рекурсивно вычисляем аргумент (на случай вложенных выражений)
            # Вычисляем значение функции
            func_value = getattr(math, func)(arg)
            # Заменяем вызов функции на результат
            s = s[:start] + str(func_value) + s[end + 1:]

    # Шаг 2: обрабатываем скобки (если остались)
    if '(' in s and ')' in s:
        start = s.rfind('(')
        end = s.find(')', start)
        if start != -1 and end != -1:
            inner_result = Calc(s[start+1:end])
            s = s[:start] + str(inner_result) + s[end+1:]
            return Calc(s)

'''    # Шаг 3: базовый разбор операций (как раньше)
    k = lastOp(s)
    if k < 0:
        return float(s)
    else:
        n1 = Calc(s[:k])
        n2 = Calc(s[k+1:])
        if s[k] == "+":
            return n1 + n2
        elif s[k] == "-":
            return n1 - n2
        elif s[k] == "*":
            return n1 * n2
        elif s[k] == "/":
            return n1 / n2
        else:
            raise ValueError(f"Неизвестная операция: {s[k]}")'''

