import re
import random

steps = []


def print_log_steps():
    for step in steps:
        print(step)


def log_step(step, details):
    steps.append(f"Step {step}: {details}")


def tokens(expression):
    return re.findall(r"(\(|\)|\+|\?|\*|\||\{[^}]*\}|\w+)", expression)


def get_string(tokens):
    string = ''
    i = 0
    step = 1
    while i < len(tokens):
        char = tokens[i]
        if char.isalnum():
            string += char
            log_step(step, f"\nProcessed character '{char}', string so far: {string}")
            i += 1
        elif char == '(':
            group = []
            i += 1
            while tokens[i] != ')' and i < len(tokens):
                group.append(tokens[i])
                i += 1
            i += 1
            log_step(step, f"Processing group {group}:")
            if i < len(tokens) and tokens[i] in ['*', '+', '?']:
                result = get_string(group)
                string += repeat(result, tokens[i])
                i += 1
                log_step(step, f"Applied operator {tokens[i]} to group, string so far: {string}")
            elif i < len(tokens) and tokens[i].startswith('{'):
                rep = tokens[i]
                rep = int(rep[1:-1])
                for _ in range(rep):
                    result = get_string(group)
                    string += repeat(result, tokens[i])
                i += 1
                log_step(step, f"Repeated group {group} {rep} times, string so far: {string}")
            else:
                string += get_string(group)
                log_step(step, f"Processed group: {group}, string so far: {string}")

        elif char == '|':
            options = [string]
            i += 1
            if tokens[i] == '(':
                group = []
                i += 1
                while tokens[i] != ')' and i < len(tokens):
                    group.append(tokens[i])
                    i += 1
                options.append(get_string(group))
            else:
                options.append(tokens[i])
            string = random.choice(options)
            i += 1
            log_step(step, f"Processed alternation '|', substring so far: {string}")
        elif tokens[i] in ['*', '+', '?']:
            group = string[-1]
            string = string[:-1] + repeat(group, tokens[i])
            log_step(step, f"Applied operator {tokens[i]} to character '{group}', string so far: {string}")
            i += 1
        elif tokens[i].startswith('{'):
            group = string[-1]
            rep = tokens[i]
            rep = int(rep[1:-1])
            for _ in range(rep - 1):
                string += repeat(group, tokens[i])
            i += 1
            log_step(step, f"Repeated character '{group}' {rep} times, string so far: {string}")
        step += 1

    return string


def repeat(group, symbol):
    if symbol == '?':
        choice = random.random()
        if choice > 0.5:
            return group
        else:
            return ''
    elif symbol == '*':
        choice = random.randint(0, 5)
        new = ''
        for _ in range(choice):
            new += group
        return new
    elif symbol == '+':
        choice = random.randint(1, 5)
        new = ''
        for _ in range(choice):
            new += group
        return new
    elif symbol.startswith('{'):
        return group
