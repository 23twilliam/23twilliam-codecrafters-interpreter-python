def Binary(left, operator, right):
    return f"({operator.lexeme} {left} {right})"

def Unary(operator, right):
    return f"({operator.lexeme} {right})"

def Literal(expr):
    def __init__(self, value):
        self.value = value

def Grouping(expr):
    return f"(group {expr})"

def expression(self):
    return self.equality()

