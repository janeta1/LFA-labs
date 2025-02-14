import random


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
