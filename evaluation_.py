from parser_ import Binary, Grouping, Literal, Unary

class Interpreter:
    def evaluate(self, expr):
        return expr.visit(self)

    def visit_literal(self, literal):
        return literal.value

    def visit_binary(self, binary):
        return NotImplementedError()

    def visit_grouping(self, grouping):
        return NotImplementedError()

    def visit_unary(self, unary):
        return NotImplementedError()
