import sys
from scanner_ import Scanner
from parser_ import Parser


def main():
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command == "tokenize":
        with open(filename) as file:
            file_contents = file.read()

        scanner = Scanner(file_contents)
        tokens, errors = scanner.scan_tokens()

        for token in tokens:
            print(token)

        for error in errors:
            print(error, file=sys.stderr)

        if errors:
            exit(65)

    elif command == "parse":
        with open(filename) as file:
            file_contents = file.read()

        scanner = Scanner(file_contents)
        tokens, errors = scanner.scan_tokens()

        parser = Parser(tokens)
        expression = parser.expression()
        for error in parser.errors:
            print(error, file=sys.stderr)
        if parser.errors:
            exit(65)

        print(expression)
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)


if __name__ == "__main__":
    main()