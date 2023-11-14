"""
#version 1
def num_permutation_sequence(n):
    result = 1
    for k in range(0, n + 1):
        yield result
        result *= (n-k)
"""

def num_permutation_sequence(n):
    result = 1
    k = 0
    while True:
        change_n = (yield result)
        if change_n == 0:
            result *= (n+1)/(n+1-k)
            n += 1
        else:
            result *= (n-k)
            k += 1  
"""
g = num_permutation_sequence(3)
assert (next(g), next(g), g.send(0), next(g), next(g), next(g), g.send(0)) == (
    1,
    3,
    4,
    12,
    24,
    24,
    120)
"""
