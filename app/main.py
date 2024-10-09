import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()
    error = False
    ptr = 0
    line_number = 1
    while ptr < len(file_contents):
        c = file_contents[ptr]
        if c == '(':
            print("LEFT_PAREN ( null")
        elif c == ')':
            print("RIGHT_PAREN ) null")
        elif c == '{':
            print("LEFT_BRACE { null")
        elif c == '}':
            print("RIGHT_BRACE } null")
        elif c == ',':
            print("COMMA , null")
        elif c == '.':
            print("DOT . null")
        elif c == '-':
            print("MINUS - null")
        elif c == '+':
            print("PLUS + null")
        elif c == ';':
            print("SEMICOLON ; null")
        elif c == '*':
            print("STAR * null")
        elif c == '=':
            if ptr < len(file_contents) - 1 and file_contents[ptr + 1] == '=':
                print("EQUAL_EQUAL == null")
                c = '=='
            else:
                print("EQUAL = null")
        elif c == '!':
            if ptr < len(file_contents) - 1 and file_contents[ptr + 1] == '=':
                print("BANG_EQUAL != null")
                c = '!='
            else:
                print("BANG ! null")
        elif c == '<':
            if ptr < len(file_contents) - 1 and file_contents[ptr + 1] == '=':
                print("LESS_EQUAL <= null")
                c = '<='
            else:
                print("LESS < null")
        elif c == '>':
            if ptr < len(file_contents) - 1 and file_contents[ptr + 1] == '=':
                print("GREATER_EQUAL >= null")
                c = '>='
            else:
                print("GREATER > null")
        elif c == '/':
            if ptr < len(file_contents) - 1 and file_contents[ptr + 1] == '/':
                while ptr < len(file_contents) and file_contents[ptr] != "\n":
                    ptr += 1
                c = '//'
                line_number += 1
            else:
                print("SLASH / null")
        elif c == " " or c == "\t":
            ptr += 1
            continue
        elif c == "\n" or c == "r":
           line_number += 1
           pass
        else:
            error = True
            print(
                "[line %s] Error: Unexpected character: %s" % (line_number, c),
                file=sys.stderr,
            )
            ptr += 1
            continue
        ptr += len(c)
    print("EOF  null")
    if error:
        exit(65)
    else:
        exit(0)


if __name__ == "__main__":
    main()
