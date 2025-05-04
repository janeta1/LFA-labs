from Lab6_ParserASTBuild.lexer import lexer
from Lab6_ParserASTBuild.Parser import *

expression1 = "((3 + 5) * 2) ^ (3 * 7) - sin(45)"
expression2 = "10 / (2 + 3) * (4 - 2) ^ 2"
expression3 = "(6 + 4) * (5 - 3) ^ sin(30)"
expression4 = "-2 ^ 3 + cos(45) * (10 / 2)"
expression5 = "sqrt(16) + (2 + 3) * (5 - 1) ^ 2"

tests = [expression1, expression2, expression3, expression4, expression5]
for expr in tests:
    print(f"\nAST tree for the expression: {expr}")
    tokens = lexer(expr)
    parser = Parser(tokens)
    ast = parser.parse_expression()
    print_ast_tree(ast)
    print("\n________________________________________________________________")
