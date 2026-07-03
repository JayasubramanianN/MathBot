from sympy import sympify
from sympy import simplify
from sympy import SympifyError


def solve_expression(expression: str):
    try:
        result = simplify(sympify(expression))
        return str(result)
    except SympifyError:
        return None
    except Exception:
        return None