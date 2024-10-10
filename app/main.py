import enum

import pathlib

import sys
from app.Tokeniser import Scanner
from typing import Any



def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)
    command = sys.argv[1]
    filename = sys.argv[2]
    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)
    file_contents = pathlib.Path(filename).read_text()
    scanner = Scanner(file_contents)
    tokens, errors = scanner.scan_tokens()
    for token in tokens:
        print(token)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        exit(65)


if __name__ == "__main__":
    main()
