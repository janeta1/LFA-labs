from Lab2_FiniteAutomata.Grammar import Grammar
from Lab2_FiniteAutomata.FiniteAutomaton import FiniteAutomaton


print("------------------Task 1------------------")
V_n = ['S', 'B', 'D']
V_t = ['a', 'b', 'c', 'd']
P = {
    'S': ['aS', 'bB'],
    'B': ['cB', 'd', 'aD'],
    'D': ['aB', 'b']
}
S = 'S'

grammar = Grammar(V_n, V_t, S, P)
print("The grammar with the production rules: ")
for non_terminal, rules in grammar.P.items():
    print(f"  {non_terminal} -> {' | '.join(rules)}")
print(f"is of type: {grammar.chomsky_type()}")


print("\n------------------Task 2------------------")
Q = ['q0', 'q1', 'q2']
E = ['a', 'b', 'c']
F = ['q2']
delta = {
    ('q0', 'a'): ['q0'],
    ('q0', 'b'): ['q1'],
    ('q1', 'c'): ['q1', 'q2'],
    ('q2', 'a'): ['q0'],
    ('q1', 'a'): ['q1']
}
fa = FiniteAutomaton(Q, E, delta, 'q0', F)
print("Finite Automata: ")
print(f"States: {fa.Q}")
print(f"Alphabet: {fa.E}")
print(f"Start state: {fa.q0}")
print(f"Final States: {fa.F}")
print("Transitions:")
for (state, symbol), next_states in fa.delta.items():
    for next_state in next_states:
        print(f"  δ({state}, {symbol}) -> {next_state}")

print("\nTransformed to Regular Grammar: ")
reg = fa.to_regular_grammar()
print(f"Non-terminals: {reg.V_n}")
print(f"Terminals: {reg.V_t}")
print(f"Start symbol: {reg.S}")
print(f"Productions:")
for non_terminal, rules in reg.P.items():
    print(f"  {non_terminal} -> {' | '.join(rules)}")

print("\n------------------Task 3------------------")
print("Checking if our Finite Automata is NFA or DFA: ")
check = fa.is_deterministic()
if check:
    print("The Finite Automata is deterministic")
else:
    print("The Finite Automata is non-deterministic")

print("\n------------------Task 4------------------")
print("Transforming the NFA to DFA: ")
print("The already known NFA: ")
for (state, symbol), next_states in fa.delta.items():
    for next_state in next_states:
        print(f"  δ({state}, {symbol}) -> {next_state}")
print("\nThe obtained DFA: ")
dfa = fa.ndfa_to_dfa()
print(f"States: {dfa.Q}")
print(f"Alphabet: {dfa.E}")
print(f"Start state: {dfa.q0}")
print(f"Final States: {dfa.F}")
print("Transitions:")
for (state, symbol), next_states in dfa.delta.items():
    print(f"  δ({state}, {symbol}) -> {next_states}")






