def Binary(left, operator, right):
    return f"({operator.lexeme} {left} {right})"

def Unary(operator, right):
    return f"({operator.lexeme} {right})"

def Literal(expr):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "nil" if self.value is None else str(self.value).lower()

def Grouping(expr):
    return f"(group {expr})"

def expression(self):
    return self.equality()

