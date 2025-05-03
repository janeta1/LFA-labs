from Lab4_RegularExpressions.lexer import *

ex1 = 'u?N{2}(O|P){3}Q*R+'
print("Example 1:")
print(f"Regular expression: {ex1}")
result = get_string(tokens(ex1))
print(f"String generated: {result}")
print("Steps: ")
print_log_steps()

print("\n                                     ...")

ex2 = '(X|Y|Z){3}8+(9|0)'
print("Example 2:")
print(f"Regular expression: {ex2}")
result = []
for _ in range(5):
    result.append(get_string(tokens(ex2)))
print(f"Strings generated: {result}")

print("\n                                     ...")

ex3 = '(H|i)(J|K)L*N?'
print("Example 3:")
print(f"Regular expression: {ex3}")
result = []
for _ in range(5):
    result.append(get_string(tokens(ex3)))
print(f"Strings generated: {result}")




