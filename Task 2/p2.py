# TDP015 Programming Assignment 2

# Do not use any imports!

# Part 1: Implement the following quantifiers. You are not allowed to use
# any libraries or built-in functions for this.

def forall(iterable, predicate):
    """Return `True` if *predicate* returns `True` for all elements of
    *iterable* (or if *iterable* is empty)."""
    for i in iterable:
        if not predicate(i):
            return False
    return True

def test_forall():
    print("test_forall")
    assert forall(set(), lambda x: False)
    assert forall(set(range(5, 10)), lambda x: x >= 5)
    assert not forall(set(range(0, 10)), lambda x: x >= 5)

def exists(iterable, predicate):
    """Return `True` if *predicate* returns `True` for at least one
    element of *iterable*."""
    # TODO: Replace the following line with your own code
    for i in iterable:
        if predicate(i):
            return True
    return False

def test_exists():
    print("test_exists")
    assert not exists(set(), lambda x: False)
    assert exists(set(range(5, 10)), lambda x: x >= 5)
    assert not exists(set(range(0, 5)), lambda x: x >= 5)

# Part 2: Implement the following functions on sets. You are not allowed
# to use any native operations on sets except for the `in` primitive.
# You are allowed to use the quantifiers from Part 1.

# How are these functions called in native Python?

def subset(s, t):
    """Test whether *s* is a subset of *t*."""
    # TODO: Replace the following line with your own code
    for i in s:
        if i not in t:
            return False
    return True

def test_subset():
    print("test_subset")
    assert subset(set(), set())
    assert subset(set(), set([0]))
    assert subset(set([0]), set([0]))
    assert subset(set([0]), set([0, 1]))
    assert not subset(set([0]), set())
    assert not subset(set([0, 1]), set([0]))

def equal(s, t):
    """Test whether *s* and *t* are equals (as sets)."""
    # TODO: Replace the following line with your own code
    if s != t:
        return False
    return True

def test_equal():
    print("test_equal")
    assert equal(set(), set())
    assert not equal(set(), set([0]))
    assert equal(set([0]), set([0]))
    assert not equal(set([0]), set([0, 1]))
    assert not equal(set([0]), set())
    assert not equal(set([0, 1]), set([0]))

def proper_subset(s, t):
    """Test whether *s* is a proper subset of *t*."""
    #TODO: Replace the following line with your own code
    return False

def test_proper_subset():
    print("test_proper_subset")
    assert not proper_subset(set(), set())
    assert proper_subset(set(), set([0]))
    assert not proper_subset(set([0]), set([0]))
    assert proper_subset(set([0]), set([0, 1]))
    assert not proper_subset(set([0]), set())
    assert not proper_subset(set([0, 1]), set([0]))

def disjoint(s, t):
    """Test whether *s* and *t* are disjoint."""
    # TODO: Replace the following line with your own code
    return False

def test_disjoint():
    print("test_disjoint")
    assert disjoint(set(), set())
    assert disjoint(set(), set([0]))
    assert not disjoint (set([0]), set([0]))
    assert not disjoint(set([0]), set([0, 1]))
    assert disjoint(set([0]), set())
    assert not disjoint(set([0, 1]), set([0]))
    assert disjoint(set([0]), set([1]))

# Part 3: Implement a Python generator that yields the subsets of a given
# set argument. In this function, you are allowed to use native methods on
# sets, but no external libraries. You may need to read up on generators.

def subsets(s):
    """Yields the subsets of the set *s*."""
    # TODO: Replace the following line with your own code
    yield None

def test_subsets():
    print("test_subsets")
    assert len(list(subsets(set()))) == 1
    assert len(list(subsets(set(range(6))))) == 64

if __name__ == '__main__':
    test_forall()
    test_exists()
    test_subset()
    test_equal()
    test_proper_subset()
    test_disjoint()
    test_subsets()
