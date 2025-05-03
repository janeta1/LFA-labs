from Lab1_RegularGrammars.Grammar import Grammar

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

