# simulating finite state machines

def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            destination = edges[(current, letter)]
            remaining_string = string[1:]
            return fsmsim(remaining_string, destination, edges, accepting)
        else:
            return False

# simulating nondeterminism
def nfsmsim(string, current, edges, accepting):
    if string =="":
        return current in accepting
    else:
        letter = string[0:1]
        if (current, letter)in edges:
            remainder = string[1:]
            newstates = edges[(current, letter)]
            for newstate in newstates:
                if nfsmsim(remainder, newstate, edges, accepting):
                    return True
        return False

# parse the string
def addtochart(theset, index, elt):
    if not (elt in theset[index]):
        theset[index] = [elt] + theset[index]
        return True
    return False

def closure(grammar, i, x, ab, cd ,j):
    next_states = [(rule[0],[], rule[1], i) for rule in grammar if cd != [] and cd[0] == rule[0]]
    return next_states

def shift(tokens, i, x, ab, cd,j):
    if cd != [] and tokens[i] == cd[0]:
        return (x, ab + [cd[0]], cd[1:], j)
    else:
        return None

def reduction(chart, i, x, ab, cd, j):
    return [(jstate[0], jstate[1] + [x], (jstate[2])[1:], jstate[3]) for jstate in chart[j] if cd==[] and jstate[2] != [] and (jstate[2])[0] == x]

def parse(tokens, grammar):
    tokens = tokens + ["end_of_input_marker"]
    chart = {}
    start_rule = grammar[0]
    for i in range(len(tokens) + 1):
        chart[i] = []
    start_state = (start_rule[0], [], start_rule[1], 0)
    chart[0] = [start_state]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart [i]
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]
                next_states = closure(grammar, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes
                next_states = reduction(chart, i, x, ab, cd, j)
                for next_state in next_states:
                    changes = addtochart(chart, i, next_state) or changes
            if not changes:
                break
    accepting_state = (start_rule[0], start_rule[1], [], 0)
    return accepting_state in chart[len(tokens)-1]


