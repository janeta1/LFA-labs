class FiniteAutomaton:
    def __init__(self, Q, E, delta, q0, F):
        self.Q = Q
        self.E = E
        self.delta = delta
        self.q0 = q0
        self.F = F

    def stringBelongToLanguage(self, inputString):
        print(self.F)
        currentState = self.q0
        currentSymbol = inputString[0]

        for i in range(len(inputString)):
            print(currentState)
            print(currentSymbol)
            if (currentState, currentSymbol) not in self.delta:
                if currentSymbol in self.F and i == len(inputString) - 1:
                    return True
                else:
                    return False
            else:
                currentState = self.delta[(currentState, currentSymbol)][0]
                currentSymbol = inputString[i + 1]


