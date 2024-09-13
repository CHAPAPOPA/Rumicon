import re


def algebraic_calculator(expression):
    """Алгебраический калькулятор"""

    def validate_expression(expression):
        """Проверка на корректность алгебраического выражения"""

        if expression.count("(") != expression.count(")"):
            return "Недопустимое выражение"

        if re.search(r"[^xyz\d\s\+\-\*\(\)]", expression):
            return "Недопустимое выражение"

        if re.search(r"\d[x|y|z]", expression):
            return "Недопустимое выражение"

        return "OK"

    def parse_and_simplify(expression):
        """Парсинг выражения и его упрощение"""

        terms = re.findall(r"[+-]?[^+-]+", expression.replace(" ", ""))
        variable_counts = {"x": 0, "y": 0, "z": 0, "const": 0}

        for term in terms:
            if "x" in term:
                variable_counts["x"] += eval(term.replace("* x", "").replace("x", "1"))
            elif "y" in term:
                variable_counts["y"] += eval(term.replace("* y", "").replace("y", "1"))
            elif "z" in term:
                variable_counts["z"] += eval(term.replace("* z", "").replace("z", "1"))
            else:
                variable_counts["const"] += eval(term)

        result = []
        if variable_counts["x"] != 0:
            result.append(
                f"{variable_counts['x']} * x" if variable_counts["x"] != 1 else "x"
            )
        if variable_counts["y"] != 0:
            result.append(
                f"{variable_counts['y']} * y" if variable_counts["y"] != 1 else "y"
            )
        if variable_counts["z"] != 0:
            result.append(
                f"{variable_counts['z']} * z" if variable_counts["z"] != 1 else "z"
            )
        if variable_counts["const"] != 0:
            result.append(str(variable_counts["const"]))

        return " + ".join(result) if result else "0"

    validation_result = validate_expression(expression)
    if validation_result != "OK":
        return validation_result

    try:
        simplified_expression = parse_and_simplify(expression)
        return simplified_expression
    except:
        return "Недопустимое выражение"


# Примеры использования
print(algebraic_calculator("2 * (3 * x + 4 * y) - 7 * y + 9"))
print(algebraic_calculator("z + z + 2 + 3 - 2 * z"))
print(algebraic_calculator("3 * (("))
print(algebraic_calculator("5x + 4y"))
