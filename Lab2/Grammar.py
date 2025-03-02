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
                    # print(currentString)
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
                if prod in self.V_t:
                    F.add(prod)

                # intermediate state
                var1 = states
                var2 = prod[0]
                for symbol in prod:
                    if symbol in self.V_t:
                        var2 = symbol
                        break
                next_state = None
                if (var1, var2) not in delta:
                    delta[(var1, var2)] = []
                for symbol in prod:
                    if symbol in self.V_n:
                        next_state = symbol
                        break
                if next_state is None:
                    next_state = 'X'

                delta[(var1, var2)].append(next_state)
        F.add('X')
        return FiniteAutomaton(Q, E, delta, q0, F)

    def chomsky_type(self):
        type = -1
        if self.type3():
            type = 3
        elif self.type2():
            type = 2
        elif self.type1():
            type = 1
        else:
            type = 0
        return type

    def type3(self):
        for non_terminal in self.P.keys():
            left_side = non_terminal
            right_side = self.P[non_terminal]
            for rule in right_side:
                if len(left_side) > 1 or len(rule) > 2:
                    return False
                elif (len(rule) == 1 and rule[0] in self.V_t) or len(rule) == 0:
                    continue
                else:
                    if rule[0] in self.V_n and rule[1] in self.V_t:
                        continue
                    elif rule[0] in self.V_t and rule[1] in self.V_n:
                        continue
                    else:
                        return False
        return True

    def type2(self):
        for non_terminal in self.P.keys():
            left_side = non_terminal
            right_side = self.P[non_terminal]
            for _ in right_side:
                if len(left_side) > 1 or left_side not in self.V_n:
                    return False
                else:
                    continue
        return True

    def type1(self):
        for non_terminal in self.P.keys():
            left_side = non_terminal
            right_side = self.P[non_terminal]
            for rule in right_side:
                if len(left_side) <= len(rule) and any(non_terminal in self.V_n for non_terminal in left_side):
                    continue
                else:
                    return False
        return True

