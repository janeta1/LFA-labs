from Lab2.Grammar import Grammar


class FiniteAutomaton:
    def __init__(self, Q, E, delta, q0, F):
        self.Q = Q
        self.E = E
        self.delta = delta
        self.q0 = q0
        self.F = F
        print(delta)
        # print(F)

    def stringBelongToLanguage(self, inputString):
        currentState = self.q0

        for symbol in inputString:
            if (currentState, symbol) in self.delta:
                currentState = self.delta[(currentState, symbol)][0]
                # print(currentState)
            else:
                return False
        return currentState in self.F

    def to_regular_grammar(self):
        V_n = list(self.delta.keys())
        V_t = self.E
        S = self.q0
        delta = {}

        for (state, terminal), next_states in self.delta.items():
            if state not in delta:
                delta[state] = []
            for next_state in next_states:
                if next_state in self.F:
                    delta[state].append(terminal)
                delta[state].append(terminal + next_state)

        for final_state in self.F:
            if final_state not in delta:
                delta[final_state] = []
            delta[final_state].append('eps')

        return Grammar(V_n, V_t, S, delta)

    def is_deterministic(self):
        repetitions = {}
        for (state, terminal), next_state in self.delta.items():
            if (state, terminal) not in repetitions:
                repetitions[(state, terminal)] = []
            for st in next_state:
                repetitions[(state, terminal)].append('+')
        for (state, terminal), value_list in repetitions.items():
            if value_list.count('+') > 1:
                return False
        return True

    def ndfa_to_dfa(self):

        return
