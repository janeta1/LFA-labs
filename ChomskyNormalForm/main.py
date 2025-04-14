from Lab1.Grammar import Grammar
from ChomskyNormalForm.cnf import Cnf

V_n = ['S', 'A', 'B', 'C', 'D']
V_t = ['a', 'b']
P = {
    "S": ["aB", "A"],
    "A": ["bAa", "aS", "a"],
    "B": ["AbB", "BS", "a", "ε"],
    "C": ["BA"],
    "D": ["a"]
}

S = 'S'

grammar = Grammar(V_n, V_t, S, P)
chomsky = Cnf()
chomsky.convert_to_cnf(grammar)

