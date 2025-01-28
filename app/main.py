import sys
from scanner_ import Scanner
from parser_ import Parser
from interpreter_ import Interpreter


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh evaluate <file>")
        sys.exit(1)

    command, file_path = sys.argv[1], sys.argv[2]
    if command != "evaluate":
        print(f"Unknown command: {command}")
        sys.exit(1)

    try:
        with open(file_path, 'r') as file:
            source = file.read()

        # Tokenize input
        scanner = Scanner(source)
        tokens, errors = scanner.scan_tokens()
        if errors:
            for error in errors:
                print(error)
            sys.exit(1)

        # Parse tokens into expressions
        parser = Parser(tokens)
        expression = parser.expression()

        # Evaluate expression
        interpreter = Interpreter()
        interpreter.interpret(expression)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()