from Lab6_ParserASTBuild.AST import *
from Lab6_ParserASTBuild.lexer import TokenType


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else ("EOF", "")

    def advance(self):
        if self.pos < len(self.tokens):
            self.pos += 1

    def expect(self, token):
        if self.current_token()[0] != token:
            raise Exception(f"Expected {token}, got {self.current_token()[0]}")
        self.advance()

    def parse_expression(self):
        node = self.parse_term()
        while self.current_token()[0] in (TokenType.ADD, TokenType.SUB):
            op = self.current_token()[1]
            self.advance()
            right = self.parse_term()
            node = BinaryOperation(node, op, right)
        return node

    def parse_term(self):
        node = self.parse_power()
        while self.current_token()[0] in (TokenType.MUL, TokenType.DIV):
            op = self.current_token()[1]
            self.advance()
            right = self.parse_power()
            node = BinaryOperation(node, op, right)
        return node

    # added separate method cause power has bigger
    # precedence than mul/div
    def parse_power(self):
        node = self.parse_factor()
        while self.current_token()[0] == TokenType.POW:
            op = self.current_token()[1]
            self.advance()
            right = self.parse_factor()
            node = BinaryOperation(node, op, right)
        return node

    def parse_factor(self):
        token, value = self.current_token()
        if token == TokenType.NUMBER:
            self.advance()
            return Number(float(value))
        elif token in (TokenType.COS, TokenType.SIN, TokenType.SQRT):
            op = value
            self.advance()
            self.expect(TokenType.LEFTP)
            right = self.parse_expression()
            self.expect(TokenType.RIGHTP)
            return UnaryOperation(op, right)
        elif token == TokenType.LEFTP:
            self.advance()
            node = self.parse_expression()
            self.expect(TokenType.RIGHTP)
            return node


