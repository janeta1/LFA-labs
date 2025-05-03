from itertools import combinations


class Cnf:
    def eliminate_epsilon_productions(self, grammar):
        new_grammar = {s: p[:] for s, p in grammar.P.items()}
        changed = True
        while changed:
            changed = False
            N_e = []

            for symbol, productions in grammar.P.items():
                for production in productions:
                    if production == "ε" and symbol != "S":
                        N_e.append(symbol)
                        changed = True
            # print(f"nulls {N_e}")

            if not N_e:
                break
            for null_p in N_e:
                # print(f"were at symbol {null_p}")
                for symbol, productions in grammar.P.items():
                    for production in productions:
                        # print(production)
                        if production.count(null_p) > 0:
                            positions = [i for i, x in enumerate(production) if x == null_p]
                            # print(positions)
                            new_production = set()
                            for r in range(1, len(positions) + 1):
                                combos = combinations(positions, r)
                                for comb in combos:
                                    new_prod = list(production)
                                    for pos in comb:
                                        new_prod[pos] = 'ε'

                                    new = ''.join([ch for i, ch in enumerate(production) if i not in comb])
                                    if new == '':
                                        new = 'ε'

                                    if new not in grammar.P[symbol]:
                                        new_production.add(new)

                                for element in new_production:
                                    if element not in new_grammar[symbol]:
                                        new_grammar[symbol].append(element)
                new_grammar[null_p].remove("ε")

            grammar.P = {s: p[:] for s, p in new_grammar.items()}
        grammar.P = new_grammar

        return grammar

    def eliminate_renaming(self, grammar):
        changed = True
        while changed:
            changed = False
            for symbol in grammar.P.keys():
                new_productions = []
                to_remove = []
                for production in grammar.P[symbol]:
                    if len(production) == 1 and production[0] in grammar.P:
                        renamed = production[0]
                        for p in grammar.P[renamed]:
                            if p not in grammar.P[symbol] and p not in new_productions:
                                new_productions.append(p)
                                changed = True
                        to_remove.append(production)
                for prod in to_remove:
                    grammar.P[symbol].remove(prod)
                grammar.P[symbol].extend(new_productions)
        return grammar

    def remove_inaccessible_symbols(self, grammar):
        accessible = set(grammar.S)
        changed = True
        while changed:
            changed = False
            current = list(accessible)
            for symbol in current:
                for production in grammar.P[symbol]:
                    for char in production:
                        if char in grammar.V_n and char not in accessible:
                            accessible.add(char)
                            changed = True
        new_P = {s: p[:] for s, p in grammar.P.items() if s in accessible}
        grammar.P = new_P
        grammar.V_n = [v for v in grammar.V_n if v in accessible]
        return grammar

    def remove_non_productive(self, grammar):
        productive = set()
        changed = True
        while changed:
            changed = False
            for symbol in grammar.P:
                for production in grammar.P[symbol]:
                    if all(s in grammar.V_t or s in productive for s in production):
                        if symbol not in productive:
                            productive.add(symbol)
                            changed = True

        new_P = {}
        for s, prods in grammar.P.items():
            if s in productive:
                filtered_prods = [p for p in prods if all(sym in grammar.V_t or sym in productive for sym in p)]
                if filtered_prods:
                    new_P[s] = filtered_prods

        grammar.P = new_P
        grammar.V_n = [v for v in grammar.V_n if v in productive]
        return grammar

    def obtain_cnf(self, grammar):
        replacements = {}
        reverse_map = {}
        counter = 1
        new_productions = {}

        for symbol in grammar.P.keys():
            new_productions.setdefault(symbol, [])
            for production in grammar.P[symbol]:
                chars = list(production)

                for i in range(len(chars)):
                    if chars[i] in grammar.V_t and len(chars) > 1:
                        terminal = chars[i]
                        if terminal not in replacements:
                            rep = f"X{counter}"
                            counter += 1
                            replacements[terminal] = rep
                            reverse_map[rep] = terminal
                            grammar.V_n.append(rep)
                            new_productions[rep] = [terminal]
                        chars[i] = replacements[terminal]

                while len(chars) > 2:
                    pair = ''.join(chars[-2:]) #last 2
                    if pair not in replacements:
                        rep = f"X{counter}"
                        counter += 1
                        replacements[pair] = rep
                        reverse_map[rep] = pair
                        grammar.V_n.append(rep)
                        new_productions[rep] = [pair]
                    chars = chars[:-2] + [replacements[pair]]

                new_productions[symbol].append(''.join(chars))
        grammar.P = new_productions
        return grammar

    def convert_to_cnf(self, grammar):
        grammar = self.eliminate_epsilon_productions(grammar)
        print("-------------------------------------------------------------------------------------")
        print("Eliminating ε productions")
        for non_terminal, rules in grammar.P.items():
            print(f"  {non_terminal} -> {' | '.join(rules)}")

        grammar = self.eliminate_renaming(grammar)
        print("-------------------------------------------------------------------------------------")
        print("Eliminating any renaming")
        for non_terminal, rules in grammar.P.items():
            print(f"  {non_terminal} -> {' | '.join(rules)}")

        grammar = self.remove_inaccessible_symbols(grammar)
        print("-------------------------------------------------------------------------------------")
        print("Eliminating inaccessible symbols")
        for non_terminal, rules in grammar.P.items():
            print(f"  {non_terminal} -> {' | '.join(rules)}")

        grammar = self.remove_non_productive(grammar)
        print("-------------------------------------------------------------------------------------")
        print("Eliminating non-productive symbols")
        for non_terminal, rules in grammar.P.items():
            print(f"  {non_terminal} -> {' | '.join(rules)}")

        grammar = self.obtain_cnf(grammar)
        print("-------------------------------------------------------------------------------------")
        print("The grammar in the Chomsky Normal Form:")
        print(f"Non-terminals: {grammar.V_n}")
        print(f"Terminals: {grammar.V_t}")
        print(f"Start symbol: {grammar.S}")
        for non_terminal, rules in grammar.P.items():
            print(f"  {non_terminal} -> {' | '.join(rules)}")
