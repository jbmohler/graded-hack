# introduction

Some thoughts on $\pi(2^n)-\pi(2^(n-1))$ where $\pi$ is the prime counting function.

# graded rings

A graded ring is a multiplicative ring $R$ with a function $f:R -> Z$ such that
for $g, h \in R$ then $f(g h)=f(g) f(h)$.

2 examples:

1. (from the obvious dept) The ring $Z$ with the function $f:i -> abs(i)$.

2. The function $F_p[x]$ with the grading function $f:g -> p ^ deg(g)$.

Note that the grading function $f$ of the polynomial ring over a finite field
with prime p elements has range of the prime powers of $p$.  Also the
cardinalities of the pre-images of this range are easy to compute (the number
of polynomials of the given degree).  Because of this structure, it is a
straight-forward combinatorial argument to compute the number of irreducible
polynomials of a given degree.

# '2-exponential banded gradings'

This exploratory code attempts to generalize from two particular graded rings -- the
natural numbers (non-negative integers) and polynomials over the finite field
with 2 elements.  Each of these have the property that they contain $2^n$
elements $x$ with grading function $f$ taken from above such that
$2^n<=f(x)<2^(n+1)$.  It is interesting to write down the the count of primes
in each of these bands for each of these fields.

Is there another graded ring with this same cardinality of elements with
grading in the bands between $2^n$.  I have not found such a ring, but perhaps
one could construct all such rings by listing the primes.
