# inspect code: http://www.pythonchallenge.com/pc/return/sequence.txt

import re
from collections import Counter

def next_value(s):
    regexp = '|'.join([str(x)+ '+' for x in range(10)])
    seq = re.findall(regexp, s)
    seq_counted = [str(x[1])+x[0] for x in [list(c.items())[0] for c in [Counter(x) for x in seq]]]
    return ''.join(seq_counted)

def compute_a(n):
    if n == 0:
        return '1'
    else:
        return next_value(compute_a(n-1))

len(compute_a(30))
