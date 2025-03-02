from Lab2.Grammar import Grammar


class FiniteAutomaton:
    def __init__(self, Q, E, delta, q0, F):
        self.Q = Q
        self.E = E
        self.delta = delta
        self.q0 = q0
        self.F = F
        # print(delta)
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
        V_n = self.Q
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

        return Grammar(V_n, V_t, S, delta)

    def is_deterministic(self):
        repetitions = {}
        for (state, terminal), next_state in self.delta.items():
            if (state, terminal) not in repetitions:
                repetitions[(state, terminal)] = []
            for _ in next_state:
                repetitions[(state, terminal)].append('+')
        for (state, terminal), value_list in repetitions.items():
            if len(value_list) > 1:
                return False
        return True

    def ndfa_to_dfa(self):
        dfa_E = self.E
        dfa_delta = {}
        dfa_q0 = {self.q0}
        dfa_F = set()
        dfa_Q = [dfa_q0]
        states_queue = [dfa_q0]

        while states_queue:
            current_dfa_state = states_queue.pop(0)

            if any(state in self.F for state in current_dfa_state):
                dfa_F.add(tuple(current_dfa_state))

            for symbol in dfa_E:
                new_state = set()

                for nfa_state in current_dfa_state:
                    # print(symbol)
                    # print(nfa_state)
                    if(nfa_state, symbol) in self.delta:
                        new_state.update(self.delta[(nfa_state, symbol)])
                # print(new_state)
                if new_state:
                    dfa_delta[(tuple(current_dfa_state), symbol)] = new_state

                    if new_state not in dfa_Q:
                        dfa_Q.append(new_state)
                        states_queue.append(new_state)
        # print(dfa_delta)
        return FiniteAutomaton(dfa_Q, dfa_E, dfa_delta, dfa_q0, dfa_F)
