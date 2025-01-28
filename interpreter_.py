from expression import Literal, expression

class Interpreter:
    def interpret(self, expr):
        if isinstance(expr, Literal):
            print(expr.value)
        else:
            raise RuntimeError("Unsupported expression type.")
