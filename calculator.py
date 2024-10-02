# calculator.py

def algebraic_calculator(expression):
    def simplify_expression(expr):
        # Шаг 1: Удаление пробелов
        expr = expr.replace(' ', '')

        # Шаг 2: Токенизация
        tokens = []
        i = 0
        while i < len(expr):
            char = expr[i]
            if char.isdigit():
                num = char
                i += 1
                while i < len(expr) and expr[i].isdigit():
                    num += expr[i]
                    i += 1
                tokens.append(num)
            elif char in ('x', 'y', 'z'):
                tokens.append(char)
                i += 1
            elif char in ('+', '-', '*', '(', ')'):
                tokens.append(char)
                i += 1
            else:
                return "Недопустимое выражение"

        if not tokens:
            return "Недопустимое выражение"

        # Шаг 3: Преобразование в обратную польскую нотацию (ОПН)
        precedence = {'+': 1, '-': 1, '*': 2}
        output_queue = []
        operator_stack = []
        try:
            for token in tokens:
                if token.isdigit():
                    output_queue.append({'type': 'number', 'value': int(token)})
                elif token in ('x', 'y', 'z'):
                    output_queue.append({'type': 'variable', 'value': token})
                elif token in precedence:
                    while (operator_stack and operator_stack[-1] in precedence and
                           precedence[operator_stack[-1]] >= precedence[token]):
                        op = operator_stack.pop()
                        output_queue.append({'type': 'operator', 'value': op})
                    operator_stack.append(token)
                elif token == '(':
                    operator_stack.append(token)
                elif token == ')':
                    while operator_stack and operator_stack[-1] != '(':
                        op = operator_stack.pop()
                        output_queue.append({'type': 'operator', 'value': op})
                    if not operator_stack or operator_stack[-1] != '(':
                        return "Недопустимое выражение"
                    operator_stack.pop()  # Удаляем '('
                else:
                    return "Недопустимое выражение"

            while operator_stack:
                op = operator_stack.pop()
                if op in ('(', ')'):
                    return "Недопустимое выражение"
                output_queue.append({'type': 'operator', 'value': op})
        except:
            return "Недопустимое выражение"

        # Шаг 4: Вычисление ОПН
        stack = []
        try:
            for token in output_queue:
                if token['type'] == 'number':
                    stack.append({'x': 0, 'y': 0, 'z': 0, 'const': token['value']})
                elif token['type'] == 'variable':
                    term = {'x': 0, 'y': 0, 'z': 0, 'const': 0}
                    term[token['value']] = 1
                    stack.append(term)
                elif token['type'] == 'operator':
                    if len(stack) < 2:
                        return "Недопустимое выражение"
                    b = stack.pop()
                    a = stack.pop()
                    if token['value'] == '+':
                        result = {
                            'x': a['x'] + b['x'],
                            'y': a['y'] + b['y'],
                            'z': a['z'] + b['z'],
                            'const': a['const'] + b['const']
                        }
                        stack.append(result)
                    elif token['value'] == '-':
                        result = {
                            'x': a['x'] - b['x'],
                            'y': a['y'] - b['y'],
                            'z': a['z'] - b['z'],
                            'const': a['const'] - b['const']
                        }
                        stack.append(result)
                    elif token['value'] == '*':
                        # Умножение только числа на термин
                        if (a['x'] == 0 and a['y'] == 0 and a['z'] == 0):
                            multiplier = a['const']
                            result = {
                                'x': multiplier * b['x'],
                                'y': multiplier * b['y'],
                                'z': multiplier * b['z'],
                                'const': multiplier * b['const']
                            }
                            stack.append(result)
                        elif (b['x'] == 0 and b['y'] == 0 and b['z'] == 0):
                            multiplier = b['const']
                            result = {
                                'x': multiplier * a['x'],
                                'y': multiplier * a['y'],
                                'z': multiplier * a['z'],
                                'const': multiplier * a['const']
                            }
                            stack.append(result)
                        else:
                            return "Недопустимое выражение"
                    else:
                        return "Недопустимое выражение"
                else:
                    return "Недопустимое выражение"

            if len(stack) != 1:
                return "Недопустимое выражение"

            final = stack.pop()
        except:
            return "Недопустимое выражение"

        # Шаг 5: Форматирование результата
        terms = []
        variables = ['x', 'y', 'z']
        for var in variables:
            coeff = final[var]
            if coeff != 0:
                if coeff == 1:
                    terms.append(f"{var}")
                elif coeff == -1:
                    terms.append(f"-{var}")
                else:
                    terms.append(f"{coeff} * {var}")
        const = final['const']
        if const != 0 or not terms:
            terms.append(str(const))

        # Формирование итогового выражения
        result = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                result += f" - {term[1:]}"
            else:
                result += f" + {term}"

        return result

    return simplify_expression(expression)


# Примеры использования
print(algebraic_calculator("2 * (3 * x + 4 * y) - 7 * y + 9"))
# Вывод: 6 * x + y + 9

print(algebraic_calculator("z + z + 2 + 3 - 2 * z"))
# Вывод: 5

print(algebraic_calculator("3 * (("))
# Вывод: Недопустимое выражение

print(algebraic_calculator("5x + 4y"))
# Вывод: Недопустимое выражение

expression = "3 * a + 5 * b + 3 * c"
print(algebraic_calculator(expression))
# Вывод: Недопустимое выражение
