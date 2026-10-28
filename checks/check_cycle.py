#!/usr/bin/env python3
"""Exact checks of the printed four-cycle block decomposition.

This verifies only finite linear algebra, not geometric or PDE claims.
No external packages are required.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


U = [[1, 0, 1, 0], [0, 1, 0, 1],
     [0, 1, 0, -1], [1, 0, -1, 0]]
assert multiply(transpose(U), U) == [[2*int(i == j) for j in range(4)]
                                    for i in range(4)]
count = 0
for a, s, t in product([F(1, 100), F(1, 3), F(2)],
                        [F(0), F(1, 10**8), F(1, 100), F(1, 4)],
                        [F(0), F(1, 10**16), F(1, 50), F(1, 4)]):
    L = [[a+t, -a, 0, -t], [-a, a+s, -s, 0],
         [0, -s, a+s, -a], [-t, 0, -a, a+t]]
    block = [[x/2 for x in row]
             for row in multiply(multiply(transpose(U), L), U)]
    expected = [[a, -a, 0, 0], [-a, a, 0, 0],
                [0, 0, a+2*t, -a], [0, 0, -a, a+2*s]]
    assert block == expected
    assert all(sum(row) == 0 for row in L)
    assert 2*a*((a+2*s)*(a+2*t)-a*a) == 4*a*a*(s+t)+8*a*s*t
    # The odd block determinant vanishes precisely when s=t=0.
    assert (((a+2*s)*(a+2*t)-a*a) == 0) == (s == t == 0)
    count += 1

# Quaternion multiplication verifies cancellation of the triplet moment.
def qm(p, q):
    a,b,c,d=p; e,f,g,h=q
    return (a*e-b*f-c*g-d*h, a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f, a*h+b*g-c*f+d*e)

i, j, jbar = (0,1,0,0), (0,0,1,0), (0,0,-1,0)
assert qm(qm(jbar, i), j) == (0,-1,0,0)
result = {'rational_cycle_cases': count, 'orthogonal_block_decomposition': True,
          'product_formula': True, 'kernel_jump': True,
          'quaternionic_pair_cancellation': True,
          'scope': 'finite formulas only; no geometric or analytic clearance'}
out = Path(__file__).with_name('cycle_results.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
