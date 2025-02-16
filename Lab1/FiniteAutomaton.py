class FiniteAutomaton:
    def __init__(self, Q, E, delta, q0, F):
        self.Q = Q
        self.E = E
        self.delta = delta
        self.q0 = q0
        self.F = F
        '''print(delta)
        print(F)'''

    def stringBelongToLanguage(self, inputString):
        currentState = self.q0

        for symbol in inputString:
            if (currentState, symbol) in self.delta:
                currentState = self.delta[(currentState, symbol)][0]
                #print(currentState)
            else:
                return False
        return currentState in self.F



