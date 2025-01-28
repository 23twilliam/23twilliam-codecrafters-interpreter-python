def Binary(left, operator, right):
    return f"({operator.lexeme} {left} {right})"

def Unary(operator, right):
    return f"({operator.lexeme} {right})"

def Literal(expr):
    if expr == None:
        return "nil"
    return str(expr).lower()

def Grouping(expr):
    return f"(group {expr})"

def expression(self):
    return self.equality()

