from token_ import Token


class Scanner:
    reserved_words = {'and': 'AND',
                      'class': 'CLASS',
                      'else': 'ELSE',
                      'false': 'FALSE',
                      'for': 'FOR',
                      'fun': 'FUN',
                      'if': 'IF',
                      'nil': 'NIL',
                      'or': 'OR',
                      'print': 'PRINT',
                      'return': 'RETURN',
                      'super': 'SUPER',
                      'this': 'THIS',
                      'true': 'TRUE',
                      'var': 'VAR',
                      'while': 'WHILE'}

    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.errors = []

    def is_at_end(self):
        return self.current >= len(self.source)

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token("EOF", "", None, self.line))
        return self.tokens, self.errors

    def scan_token(self):
        c = self.advance()
        match c:
            case "(":
                self.add_token("LEFT_PAREN")
            case ")":
                self.add_token("RIGHT_PAREN")
            case "{":
                self.add_token("LEFT_BRACE")
            case "}":
                self.add_token("RIGHT_BRACE")
            case "*":
                self.add_token("STAR")
            case ".":
                self.add_token("DOT")
            case ",":
                self.add_token("COMMA")
            case "+":
                self.add_token("PLUS")
            case "-":
                self.add_token("MINUS")
            case ";":
                self.add_token("SEMICOLON")
            case "=":
                if self.match("="):
                    self.add_token("EQUAL_EQUAL")
                else:
                    self.add_token("EQUAL")
            case "!":
                if self.match("="):
                    self.add_token("BANG_EQUAL")
                else:
                    self.add_token("BANG")
            case ">":
                if self.match("="):
                    self.add_token("GREATER_EQUAL")
                else:
                    self.add_token("GREATER")
            case "<":
                if self.match("="):
                    self.add_token("LESS_EQUAL")
                else:
                    self.add_token("LESS")
            case "/":
                if self.match("/"):
                    while self.peek() != '\n' and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token("SLASH")
            case ' ' | '\r' | '\t':
                next
            case '\n':
                self.line += 1
            case '"':
                self.string()
            case _:
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier()
                else:
                    self.error(f"Unexpected character: {c}")

    def is_alpha(self, c):
        return ('a' <= c <= 'z') or ('A' <= c <= 'Z') or c == '_'

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        text = self.source[self.start: self.current]
        type = self.reserved_words.get(text)
        if type == None:
            type = "IDENTIFIER"

        self.add_token(type)

    def is_alpha_numeric(self, c):
        return self.is_digit(c) or self.is_alpha(c)

    def is_digit(self, c):
        return '0' <= c <= '9'

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()
        if self.peek() == '.' and self.is_digit(self.peekNext()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()

        self.add_token('NUMBER', float(self.source[self.start: self.current]))

    def peekNext(self):
        if (self.current + 1) >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()

        if self.is_at_end():
            self.error("Unterminated string.")
            return
        self.advance()
        value = self.source[self.start + 1: self.current - 1]
        self.add_token('STRING', value)

    def match(self, expected):
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def add_token(self, type, literal=None):
        token = self.source[self.start: self.current]
        self.tokens.append(Token(type, token, literal, self.line))

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def error(self, message):
        self.errors.append(f"[line {self.line}] Error: {message}")
