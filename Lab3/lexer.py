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





