from Lab2.Grammar import Grammar
from Lab2.FiniteAutomaton import FiniteAutomaton


V_n = ['S', 'B', 'D']
V_t = ['a', 'b', 'c', 'd']
P = {
    'S': ['aS', 'bB'],
    'B': ['cB', 'd', 'aD'],
    'D': ['aB', 'b']
}

S = 'S'

grammar = Grammar(V_n, V_t, S, P)
words = []
print("Words generated from the grammar: ")
for _ in range(5):
    words.append(grammar.generate_strings())
print(words)
print('\nChecking if the generated words truly belong to the grammar: ')
fa = grammar.toFiniteAutomaton()
for i in range(len(words)):
    print(words[i] + ': ' + str(fa.stringBelongToLanguage(words[i])))
print('\nChecking words that dont belong to the grammar to see if the function works: ')
new_words = ['bacccd', 'b', 'abababc']
for i in range(len(new_words)):
    print(new_words[i] + ': ' + str(fa.stringBelongToLanguage(new_words[i])))

print(grammar.chomsky_type())


Q = ['q0', 'q1', 'q2']
E = ['a', 'b', 'c']
F = ['q2']
delta = {
    ('q0', 'a'): ['q0', 'q2'],
    ('q0', 'b'): ['q1'],
    ('q1', 'c'): ['q1'],
    ('q1', 'c'): ['q2'],
    ('q2', 'a'): ['q0'],
    ('q1', 'a'): ['q1']
}

fa = FiniteAutomaton(Q, E, delta, 'q0', F)
reg = fa.to_regular_grammar()
print(reg.P)
print(fa.is_deterministic())


