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


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.errors = []

    def expression(self):
        return self.equality()

    def equality(self):
        expr = self.comparison()

        while (self.match(["BANG_EQUAL", "EQUAL_EQUAL"])):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self):
        expr = self.term()

        while (self.match(["GREATER", "GREATER_EQUAL", "LESS", "LESS_EQUAL"])):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()

        while (self.match(["SLASH", "STAR"])):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self):
        if self.match(["BANG", "MINUS"]):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)

        return self.primary()

    def primary(self):
        if self.match(["FALSE"]):
            return Literal(False)
        if self.match(["TRUE"]):
            return Literal(True)
        if self.match(["NIL"]):
            return Literal(None)

        if self.match(["NUMBER", "STRING"]):
            return Literal(self.previous().literal)
        if self.match(["LEFT_PAREN"]):
            expr = self.expression()
            self.consume("RIGHT_PAREN", "Unmatched parentheses.")
            return Grouping(expr)
        self.error(self.peek(), "Expect expression")

    def term(self):
        expr = self.factor()
        while self.match(["MINUS", "PLUS"]):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def match(self, types):
        for type in types:
            if self.check(type):
                self.advance()
                return True

        return False

    def check(self, type):
        if self.is_at_end():
            return False
        return self.peek().type == type

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == "EOF"

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def consume(self, type, message):
        if (self.check(type)):
            return self.advance()
        self.error(self.peek(), message)

    def error(self, token, message):
        self.errors.append(f"[line {token.line}] Error: {message}")
