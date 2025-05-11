class Number:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class UnaryOperation:
    def __init__(self, op, right):
        self.op = op
        self.right = right


def print_ast_tree(node, prefix="", is_tail=True):
    connector = "└── " if is_tail else "├── "

    if isinstance(node, Number):
        print(prefix + connector + f"{node.value}")

    elif isinstance(node, UnaryOperation):
        print(prefix + connector + f"{node.op}")
        print_ast_tree(node.right, prefix + ("    " if is_tail else "│   "), True)

    elif isinstance(node, BinaryOperation):
        print(prefix + connector + f"{node.op}")
        print_ast_tree(node.left, prefix + ("    " if is_tail else "│   "), False)
        print_ast_tree(node.right, prefix + ("    " if is_tail else "│   "), True)

    else:
        print(prefix + connector + "Unknown node")
