from expr_ import Literal, expression

class Interpreter:

    def interpret(self, expr: expression):
        if isinstance(expr, Literal):
            print(expr.value)
