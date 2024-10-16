class Token:

    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        literal_str = "null" if self.literal is None else str(self.literal)
        return f"{str(self.type)} {self.lexeme} {literal_str}"
