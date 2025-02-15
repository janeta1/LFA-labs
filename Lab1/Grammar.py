import random

from Lab1.FiniteAutomaton import FiniteAutomaton


class Grammar:

    def __init__(self, V_n, V_t, S, P):
        self.V_n = V_n
        self.V_t = V_t
        self.S = S
        self.P = P

    def generate_strings(self):
        currentString = self.S

        while True:
            all_terminals = True

            for i in range(len(currentString)):
                symbol = currentString[i]
                if symbol in self.V_n:
                    replacement = random.choice(self.P[symbol])
                    currentString = currentString.replace(symbol, replacement, 1)
                    print(currentString)
                    all_terminals = False


            if all_terminals:
                break

        return currentString

    def toFiniteAutomaton(self):
        E = self.V_t
        Q = self.V_n
        q0 = self.S
        F = set()
        delta = {}

        for states, productions in self.P.items():
            for prod in productions:
                # final state
                if prod in V_t:
                    F.add(prod)
                else:
                    # intermediate state
                    var1 = states
                    var2 = prod[0]

                    if (var1, var2) not in delta:
                        delta[(var1, var2)] = []
                    delta[(var1, var2)] = prod[1]

        return FiniteAutomaton(Q, E, delta, q0, F)


V_n = 'SBD'
V_t = 'abcd'
P = {
    'S': ['aS', 'bB'],
    'B': ['cB', 'd', 'aD'],
    'D': ['aB', 'b']
}

S = 'S'

grammar = Grammar(V_n, V_t, S, P)
for _ in range(1):
    print('result: ' + grammar.generate_strings())

string = grammar.generate_strings()
print('String: ' + string)
fa = grammar.toFiniteAutomaton()
print(fa.stringBelongToLanguage('string'))
