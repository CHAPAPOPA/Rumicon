import re


class AlgebraicCalculator:
    """Улучшенный калькулятор"""

    def __init__(self, expression):
        self.expression = expression
        self.variables = {"x": 0, "y": 0, "z": 0}

    def validate_expression(self):
        """Функция проверки корректности выражения"""
        if self.expression.count("(") != self.expression.count(")"):
            return "Недопустимое выражение"

        if re.search(r"[^xyz\d\s\+\-\*\(\)]", self.expression):
            return "Недопустимое выражение"

        if re.search(r"\d[x|y|z]", self.expression):
            return "Недопустимое выражение"

        return "OK"

    def simplify(self):
        """Функция улучшения выражения"""
        validation_result = self.validate_expression()
        if validation_result != "OK":
            return validation_result

        try:
            eval(self.expression, {"x": 1, "y": 1, "z": 1})
        except Exception:
            return "Недопустимое выражение"

        simplified_expression = self._simplify_variables()

        return simplified_expression

    def _simplify_variables(self):
        """Функция улучшения переменных"""
        terms = re.findall(r"[+-]?[^+-]+", self.expression.replace(" ", ""))

        counter = {"x": 0, "y": 0, "z": 0, "num": 0}

        for term in terms:
            if "x" in term:
                counter["x"] += self._evaluate_term(term, "x")
            elif "y" in term:
                counter["y"] += self._evaluate_term(term, "y")
            elif "z" in term:
                counter["z"] += self._evaluate_term(term, "z")
            else:
                try:
                    counter["num"] += eval(term)
                except Exception:
                    return "Недопустимое выражение"

        result = []
        if counter["x"] != 0:
            result.append(f"{counter['x']} * x" if counter["x"] != 1 else "x")
        if counter["y"] != 0:
            result.append(f"{counter['y']} * y" if counter["y"] != 1 else "y")
        if counter["z"] != 0:
            result.append(f"{counter['z']} * z" if counter["z"] != 1 else "z")
        if counter["num"] != 0:
            result.append(str(counter["num"]))

        return " + ".join(result) if result else "0"

    def _evaluate_term(self, term, variable):
        """Функция вычисления коэффициента"""
        if "*" in term:
            coeff = term.split("*")[0].strip()
        else:
            coeff = term.replace(variable, "").strip()

        try:
            return eval(coeff) if coeff else 1
        except Exception:
            return 1


# Пример использования
calc1 = AlgebraicCalculator("2 * (3 * x + 4 * y) - 7 * y + 9")
print(calc1.simplify())

calc2 = AlgebraicCalculator("z + z + 2 + 3 - 2 * z")
print(calc2.simplify())

calc3 = AlgebraicCalculator("3 * (")
print(calc3.simplify())

calc4 = AlgebraicCalculator("5x + 4y")
print(calc4.simplify())
