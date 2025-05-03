import re


TOKENS = [
    ("NUMBER", r"[+-]?\d+(\.\d+)?"),
    ("SUB", r"\-"),
    ("ADD", r"\+"),
    ("DIV", r"\/"),
    ("MUL", r"\*"),
    ("SIN", r"sin"),
    ("COS", r"cos"),
    ("POW", r"\^"),
    ("SQRT", r"sqrt"),
    ("LEFTP", r"\("),
    ("RIGHTP", r"\)"),
    ("SPACE", r"\s+")
]

regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKENS)


def lexer(expression):
    tokens = []

    for match in re.finditer(regex, expression):
        kind = match.lastgroup
        token = match.group()

        if kind == "SPACE":
            continue
        else:
            tokens.append((kind, token))

    return tokens


print("1. Expression: 5*cos(8) + sqrt(9) - 19.4")
print("Result: ")
print(lexer("5*cos(8) + sqrt(9) - 19.4"))
print("                                                                                   ...")
print("2. Expression: (1+2)/3 -3^6+4*sin(sqrt(3))")
print("Result: ")
print(lexer("(1+2)/3 -3^6+4*sin(sqrt(3))"))
print("                                                                                   ...")
print("3. Expression: 1.19 / sqrt(9^2)")
print("Result: ")
print(lexer("1.19 / sqrt(9^2)"))
