# LAB 2: Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.

### Course: Formal Languages & Finite Automata
### Author: Janeta Grigoras

----

## Theory
A finite automaton (FA) is a computational model used to
represent processes or systems that transition between different
states based on inputs. It can be likened to a state machine, as both
share a similar structure and purpose of modeling dynamic systems.
The term "finite" refers to the fact that an automaton has a finite
number of states, including a starting state and a set of final states,
signifying that a process modeled by an automaton has a clear beginning and an end.

Depending on the transitions between states, a finite automaton may exhibit
non-determinism. This occurs when a single transition can lead to multiple
possible next states. Non-determinism refers to a situation where the
outcome is not solely determined by the current state and input, and
this introduces uncertainty in the system's behavior. On the other hand,
determinism describes a system where, given a particular state and input,
the next state is uniquely determined.

In the context of automata, it is possible to convert a non-deterministic finite automaton (NFA) into a deterministic finite automaton (DFA) using specific algorithms. This transformation eliminates the ambiguity in state transitions and results in a model that behaves predictably.



## Objectives:

---
1. Understand what an automaton is and what it can be used for.


2. Continuing the work in the same repository and the same project, 
the following need to be added:

   a. Provide a function in your grammar type/class that could classify the 
   grammar based on Chomsky hierarchy. 

   b. For this you can use the variant from the previous lab.


3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:

    a. Implement conversion of a finite automaton to a regular grammar.
    
    b. Determine whether your FA is deterministic or non-deterministic.
    
    c. Implement some functionality that would convert an NDFA to a DFA.
    
    d. Represent the finite automaton graphically (Optional, and can be considered as a bonus point):

      - You can use external libraries, tools or APIs to generate the figures/diagrams.
      
      - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.

## Implementation description

---
### Task 1: Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy
I used the grammar from the previous lab to help me write the function:

```
VN={S, B, D}, 
VT={a, b, c, d}, 
P={ 
    S → aS
    S → bB
    B → cB
    B → d
    B → aD
    D → aB
    D → b
}
```
I wrote the function chomsky_type(), which determines the 
Chomsky Normal Form (CNF) type of given grammar. It calls 
the helper functions type3(), type2(), and type1() to check 
for Type 3, Type 2, Type 1 or Type 0 grammar, respectively.

```python
def chomsky_type(self):
    if self.type3():
        return 3
    elif self.type2():
        return 2
    elif self.type1():
        return 1
    else:
        return 0
```
**In the chomsky_type(self) function:**
- I first check if the grammar satisfies the conditions for 
Type 3 (Regular Grammar) by calling the function type3(). 
If it does, I return 3 to indicate that the grammar is Type 3.
- If type3() returns False, I then check for Type 2 
(Context-Free Grammar) by calling the function type2(). 
If it returns True, I return 2 to indicate that the grammar 
is Type 2.
- If neither type3() nor type2() returns True, I proceed to 
check for Type 1 (Context-Sensitive Grammar) by calling the 
function type1(). If type1() returns True, I return 1 to 
indicate that the grammar is Type 1.
- If none of these functions return True, I return 0 to indicate
that the grammar is Type 0.


**The helper functions:**

* ```python
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
    ```
    This function checks if the grammar is Type 3 
    (Regular Grammar). A grammar is Type 3 if:

    - Each production rule must have at most two symbols on the right-hand side.
    - The rule can either be of the form A -> a (where A is a non-terminal and a is a terminal), or A -> Ba or A -> aB (where B is a non-terminal and a is a terminal). In type3(), I iterate over all production rules in self.P:
      - If the left-hand side has more than one character or the right-hand side has more than two characters, I return False.
      - I check if the rules are of the form A -> a, A -> Ba, or A -> aB. If they meet these conditions, the grammar is Type 3, and I return True.

* ```python
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
    ```
    This function checks if the grammar is Type 2 
(Context-Free Grammar). For a grammar to be Type 2:

  - The left-hand side of each production rule must 
  consist of a single non-terminal.
  - The right-hand side can have any number of symbols (both terminals and non-terminals). In type2(), I iterate through the production rules:
    - If the left-hand side contains more than one symbol or is not a non-terminal, I return False.
    - If the left-hand side is a single non-terminal and the rule satisfies the conditions, I continue and eventually return True.

* ```python
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
    ```
    This function checks if the grammar is Type 1 (Context-Sensitive Grammar). For a grammar to be Type 1:
  - The length of the left-hand side of each production rule is less than or equal to the length of the right-hand side.
  - The left-hand side may contain non-terminal symbols. In type1(), I iterate through all production rules:
    - If the length of the left-hand side is greater than the right-hand side, I return False.
    - I check that the left-hand side contains non-terminals.
    - If all rules meet the conditions, I return True.

This structure allows me to classify the given grammar into the correct Chomsky Normal Form type by verifying each type's conditions step by step.
### Task 2: Implement conversion of a finite automaton to a regular grammar
For Task 2, 3, and 4, I implemented the finite automaton from variant 14 to help me test my code later.
Moreover, I used the FiniteAutomaton class created in the last lab and added the new functions to implement the required tasks.
```
Q = {q0,q1,q2},
∑ = {a,b,c},
F = {q2},
δ(q0,a) = q0,
δ(q0,b) = q1,
δ(q1,c) = q1,
δ(q1,c) = q2,
δ(q2,a) = q0,
δ(q1,a) = q1.
```
I wrote the function to_regular_grammar(self), which converts a finite automaton (FA) into a regular grammar. A regular grammar consists of a set of production rules where the right-hand side of each rule contains at most one non-terminal symbol, optionally followed by a terminal symbol.
```python
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
```
**How it works:**
1. Input:
   - The function uses the attributes of the finite automaton (FA) object:
     - self.Q: The set of states in the FA.
     - self.E: The input alphabet in the FA.
     - self.q0: The initial state of the FA.
     - self.delta: The transition function, represented as a dictionary where keys are pairs of (state, terminal) and values are the set of next states.
     - self.F: The set of final states in the FA.

2. Initialization:
   - ```V_n = self.Q```: The non-terminal set (V_n) is the set of states in the FA.
   - ```V_t = self.E```: The terminal set (V_t) is the input alphabet of the FA.
   - ```S = self.q0```: The start symbol of the grammar is the initial state of the FA (self.q0).
   - ```delta = {}```: A new dictionary delta is created to store the production rules for the grammar.

3. Building the Grammar:
   - The function iterates through the delta transitions of the FA.
     - For each pair (state, terminal) in the transition function, the next states are fetched.
     - If the next state is a final state, a production rule is added that consists only of the terminal.
     - For non-final states, the production rule consists of the terminal followed by the next state (as a non-terminal).
   - This ensures that each transition in the FA corresponds to a production in the grammar.
4. Finally, a Grammar object is created and returned, which contains the following:
   - V_n: The set of non-terminals (states).
   - V_t: The set of terminals (alphabet).
   - S: The start symbol (initial state).
   - delta: The production rules dictionary.

### Task 3: Determine whether your FA is deterministic or non-deterministic
Next, I implemented the is_deterministic() function to check whether my FA is deterministic (DFA) or non-deterministic (NDFA/NFA). 
A deterministic automaton has only one possible transition for each state and input symbol. If there are multiple transitions for the same state and input symbol, it is non-deterministic.
```python
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
```
**How it works:**
1. Tracking Transitions:
    - The function uses a dictionary called repetitions to store the transitions. The key is a pair of (state, input symbol) and the value is a list of next states.
    - Whenever it finds a transition, it adds a '+' to the list of next states for that (state, terminal) pair.
2. Checking Transitions:
   - After going through all the transitions, the function checks if any pair (state, terminal) has more than one '+' in its list.
   - If a pair has more than one '+', it means there is more than one possible next state for that (state, terminal) combination. This makes the automaton non-deterministic, so the function returns False.
3. Result:
   - If all state and input symbol pairs have only one '+' (or no transitions at all), it means the automaton is deterministic, so the function returns True.
### Task 4: Implement some functionality that would convert an NDFA to a DFA
For this task, I implemented the function ndfa_to_dfa() to convert a non-deterministic finite automaton into a deterministic finite automaton.
The main idea behind this conversion is to represent the multiple possible states of the NDFA in a single state of the DFA. This process is called subset construction.
```python
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
                if(nfa_state, symbol) in self.delta:
                    new_state.update(self.delta[(nfa_state, symbol)])
            if new_state:
                dfa_delta[(tuple(current_dfa_state), symbol)] = new_state

                if new_state not in dfa_Q:
                    dfa_Q.append(new_state)
                    states_queue.append(new_state)
    return FiniteAutomaton(dfa_Q, dfa_E, dfa_delta, dfa_q0, dfa_F)
```
**How it works:**
1. Initialization:
   - dfa_E: The alphabet (set of symbols) of the DFA is the same as that of the NDFA (self.E).
   - dfa_q0: The start state of the DFA is the set containing the start state of the NDFA (self.q0).
   - dfa_F: The set of final states for the DFA, initially empty.
   - dfa_Q: A list of states for the DFA, starting with dfa_q0.
   - states_queue: A queue to help explore new states, initially containing dfa_q0.
2. Processing each state:
   - The function enters a while loop, processing states in states_queue. For each state in the queue:
     - If any of the states in the current DFA state are final states in the NDFA (self.F), the DFA state is added to dfa_F.
     - The function then checks each symbol in the DFA alphabet (dfa_E), and for each symbol, it computes the next state:
       - It iterates through the NDFA states in the current DFA state and checks for transitions based on the symbol.
       - If a transition exists in the NDFA ((nfa_state, symbol) in self.delta), the next state is updated with all the possible states that can be reached from the current states.
3. Updating DFA states:
   - If a new state is reached (new_state), it is added to the DFA's transition table (dfa_delta), where the key is the tuple (tuple(current_dfa_state), symbol) and the value is the new state.
   - If this new state has not been encountered before (i.e., it's not in dfa_Q), it is added to dfa_Q and states_queue for further exploration.
4. Returning the DFA:
   - After all states are processed, a new FiniteAutomaton object is returned with the following components:
     - dfa_Q: The set of DFA states.
     - dfa_E: The alphabet of the DFA.
     - dfa_delta: The transition function of the DFA.
     - dfa_q0: The start state of the DFA.
     - dfa_F: The set of final states of the DFA.
## Conclusions / Screenshots / Results
* To test my functions, I created a main file.
  * For task 1, I used the grammar from the last lab and then determined its Chomsky type with the function chomsky_type(). The result correctly identified the grammar as of type 3 (Context-Free Grammar).
  * <img src="./task1.png">
  * For task 2, I implemented the finite automaton from Variant 14, and then converted it into a regular grammar with the function to_regular_grammar(). The output correctly displayed the automaton’s components and the transformed regular grammar with proper non-terminals, terminals, and production rules.
  * <img src="./task2.png">
  * For task 3, I checked whether the finite automaton is deterministic or non-deterministic using the is_deterministic() method. The output correctly identified the automaton as non-deterministic.
  * <img src="./task3.png">
  * For task 4, I converted the NFA into a DFA using subset construction. The output correctly showed the transformation, displaying the DFA's states, alphabet, transitions, and final states. The results seem correct based on the expected DFA conversion process.
  * <img src="./task4.png">
* In conclusion, this laboratory work helped me understand key concepts like grammars, finite automata, and the conversion between NFA and DFA. I learned how to determine whether an automaton is deterministic and how to transform it into a regular grammar, which is essential for simplifying computational models. This knowledge will be useful in future projects involving language recognition, text processing, and algorithm optimization. Additionally, it will play a crucial role in my ELSD (Elaborating Domain-Specific Languages) course, where I’ll need to design parsers and interpreters for custom languages. These concepts will allow me to create more efficient and domain-specific solutions tailored to specific tasks.
## References
* [Chomsky Classification of Grammars](https://www.tutorialspoint.com/automata_theory/chomsky_classification_of_grammars.htm)
* [Converting Finite Automata to Regular Grammar](https://www.youtube.com/watch?v=hJIVmVAJhL4&ab_channel=SudhakarAtchala)
* [NDFA to DFA Conversion](https://www.tutorialspoint.com/automata_theory/ndfa_to_dfa_conversion.htm)
* [Converting NFA to DFA](https://www.youtube.com/watch?v=6aOtnyL40X8&list=PLXj4XH7LcRfBkMlS_9aebcY78NLFwhE4M&index=35&ab_channel=SudhakarAtchala)