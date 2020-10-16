import collections


class Element:
    def __init__(self):
        raise RuntimeError("construct elements by multiplying primes")

    @staticmethod
    def zero():
        result = Element.__new__(Element)
        result.grade = 0
        result.primes = None
        return result

    @staticmethod
    def one():
        result = Element.__new__(Element)
        result.grade = 1
        result.primes = []
        return result

    def __str__(self):
        if self == 0:
            return "(0)"
        elif self == 1:
            return "(1)"
        return f"({' '.join([str(p) for p in self.primes])})"

    def __mul__(self, other):
        # multiplication is commutative

        if self == 0 or other == 0:
            return Element.zero()
        if self == 1:
            return other
        if other == 1:
            return self

        result = Element.__new__(Element)
        result.grade = self.grade * other.grade
        result.primes = self.primes + other.primes
        result.primes.sort(key=lambda x: x.lex)
        return result

    def __eq__(self, other):
        if type(other) is int:
            assert other in (0, 1)

            return self.grade == other

        return self.grade == other.grade and all(
            [p1 == p2 for p1, p2 in zip(self.primes, other.primes)]
        )


class Prime(Element):
    def __init__(self, grade, ref):
        self.grade = grade
        self.ref = ref

    @property
    def lex(self):
        return (self.grade, self.ref)

    def __str__(self):
        return f"P{self.grade}_{self.ref}"

    @property
    def primes(self):
        return [self]


pp = Prime

"""

p3a = pp(3, 'a')
p3b = pp(3, 'b')
p2a = pp(2, 'a')

print(p3a)
print(p3a*p2a)
print(p3a*Element.zero())
print((p3a*p2a*p3a*Element.one()).grade)
print(p3a*p2a*p3b)
"""


def place_grade(grade, required, primes):
    placements = 2 ** grade
    base = placements

    # compute required from primes
    def _count(pp, menu, gmin, gmax):
        if len(menu) == 0:
            return
        p = menu[0]
        for _ in range(gmax // p.grade):
            yield from _count(pp, menu[1:], gmin, gmax)
            pp *= p
            if gmin <= pp.grade < gmax:
                yield pp

    requirements = collections.defaultdict(lambda: [])
    for elt in _count(Element.one(), primes, placements, 2 * placements):
        print(elt, elt.grade)
        requirements[elt.grade].append(elt)

    if grade == 3:
        return

    # iterate through all the integer tuples of length `placement` with a sum
    # of exactly `placement`

    prodcounts = [
        len(requirements[grade]) for grade in range(placements, 2 * placements)
    ]
    if sum(prodcounts) > placements:
        return

    def _enum(index, counts, remaining):
        nonlocal prodcounts

        if remaining == 0:
            counts[index : len(counts)] = [0] * (len(counts) - index)
            yield counts
        elif index == len(counts) - 1:
            counts[index] = remaining
            yield counts
        else:
            for i in range(remaining, -1, -1):
                counts[index] = i
                yield from _enum(index + 1, counts, remaining - i)

    counts = [0] * placements

    for xx in _enum(0, counts, placements - sum(prodcounts)):
        print(xx)
        _p = primes.copy()
        for offset, count in enumerate(xx):
            for i in range(count):
                _p.append(pp(base + offset, chr(97 + i)))
        if grade < 3:
            place_grade(grade + 1, None, _p)


if __name__ == "__main__":
    for x in range(1, 2):
        place_grade(x, {}, [])
