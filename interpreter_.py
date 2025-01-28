from expression import Literal, expression

class Interpreter:

    def interpret(self, expr):
        try:
            value = self.evaluate(expr)
            print(value)
        except RuntimeError as error:
            print(f"[Runtime Error] {error}")

    def evaluate(self, expr):
        if isinstance(expr, Literal):
            return expr.value
        else:
            raise RuntimeError("Unsupported expression type.")
