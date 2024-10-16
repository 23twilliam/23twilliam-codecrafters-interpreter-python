

class Interpreter():
    def interpret(self, expr: Expr) -> None:
        if isinstance(expr, LiteralExpr):
            print(expr.value)
