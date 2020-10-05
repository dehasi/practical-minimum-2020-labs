# regex=a*b*c*
"""
|  \  |  a  | b  |   c |
|:---:|:---:|:---:|:---:|
| S0  | S0  | S1  | S2  |
| S1  |     | S1  | S2  |
| S2  |     |     | S2  |
"""
TRANSITIONS = {
    "S0": {"a": "S0", "b": "S1", "c": "S2"},
    "S1": {"b": "S1", "c": "S2"},
    "S2": {"c": "S2"}
}
START_STATE = {"a": "S0", "b": "S1", "c": "S2"}
END_STATE = {"S0", "S1", "S2"}


def match(input):
    if input[0] not in START_STATE: return False

    i = 0
    state = START_STATE[input[i]]
    while i < len(input):
        if state not in TRANSITIONS: return False
        if input[i] not in TRANSITIONS[state]: return False

        state = TRANSITIONS[state][input[i]]; i += 1
    return state in END_STATE


assert match("c")
assert match("bc")
assert match("ac")
assert match("aaaabbc")
assert match("aaaabbcccc")

assert not match("e")
assert not match("bca")
assert not match("aaaabbgc")

print("LOL! It works!")
