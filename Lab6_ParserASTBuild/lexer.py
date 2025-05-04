import re
from enum import Enum

class TokenType(Enum):
    NUMBER = r"[+-]?\d+(\.\d+)?"
    SUB = r"\-"
    ADD = r"\+"
    DIV = r"\/"
    MUL = r"\*"
    SIN = r"sin"
    COS = r"cos"
    POW = r"\^"
    SQRT = r"sqrt"
    LEFTP = r"\("
    RIGHTP = r"\)"
    SPACE = r"\s+"


regex = "|".join(f"(?P<{token.name}>{token.value})" for token in TokenType)


def lexer(expression):
    tokens = []

    for match in re.finditer(regex, expression):
        kind = match.lastgroup
        value = match.group()

        if kind == "SPACE":
            continue
        else:
            tokens.append((TokenType[kind], value))

    return tokens
