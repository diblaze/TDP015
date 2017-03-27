import itertools
import unittest


class Exp(object):
    """A Boolean expression.

    A Boolean expression is represented in terms of a *reserved symbol* (a
    string) and a list of *subexpressions* (instances of the class `Exp`).
    The reserved symbol is a unique name for the specific type of
    expression that an instance of the class represents. For example, the
    constant `True` uses the reserved symbol `1`, and logical and uses `∧`
    (the Unicode symbol for conjunction). The reserved symbol for a
    variable is its name, such as `x` or `y`.

    Attributes:
        sym: The reserved symbol of the expression (a string).
        sexps: The list of subexpressions (instances of the class `Exp`).
    """

    def __init__(self, sym, *sexps):
        """Constructs a new expression.

        Args:
            sym: The reserved symbol for this expression.
            sexps: The list of subexpressions.
        """
        self.sym = sym
        self.sexps = sexps

    def value(self, assignment):
        """Returns the value of this expression under the specified truth
        assignment.

        Args:
            assignment: A truth assignment, represented as a dictionary
            that maps variable names to truth values.

        Returns:
            The value of this expression under the specified truth
            assignment: either `True` or `False`.
        """
        raise ValueError()

    def variables(self):
        """Returns the (names of the) variables in this expression.

        Returns:
           The names of the variables in this expression, as a set.
        """
        variables = set()
        for sexp in self.sexps:
            variables |= sexp.variables()
        return variables


class Var(Exp):
    """A variable."""

    def __init__(self, sym):
        super().__init__(sym)

    def value(self, assignment):
        assert len(self.sexps) == 0
        return assignment[self.sym]

    def variables(self):
        assert len(self.sexps) == 0
        return {self.sym}


class Nega(Exp):
    """Logical not."""

    def __init__(self, sexp1):
        super().__init__('-|', sexp1)

    def value(self, assignment):
        assert len(self.sexps) == 1
        return \
            not self.sexps[0].value(assignment)


class Conj(Exp):
    """Logical and."""

    def __init__(self, sexp1, sexp2):
        super().__init__('∧', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            self.sexps[0].value(assignment) and \
            self.sexps[1].value(assignment)


class Disj(Exp):
    """Logical or."""

    def __init__(self, sexp1, sexp2):
        super().__init__('v', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            self.sexps[0].value(assignment) or self.sexps[1].value(assignment)


class Impl(Exp):
    """Logical implication."""

    def __init__(self, sexp1, sexp2):
        super().__init__('->', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            (self.sexps[0].value(assignment) and self.sexps[1].value(assignment)) or \
            (self.sexps[1].value(assignment) and not self.sexps[0].value(assignment)) or \
            (not self.sexps[1].value(assignment) and not self.sexps[0].value(assignment))


class Equi(Exp):
    """Logical equivalence."""

    def __init__(self, sexp1, sexp2):
        super().__init__('<->', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            (self.sexps[0].value(assignment) == self.sexps[1].value(assignment))

    # TODO: Complete this class


def assignments(variables):
    """Yields all truth assignments to the specified variables.

    Args:
        variables: A set of variable names.

    Yields:
        All truth assignments to the specified variables. A truth
        assignment is represented as a dictionary mapping variable names to
        truth values. Example:

        {'x': True, 'y': False}
    """
    # TODO: Complete this function. Use the itertools module!

    for combination in itertools.product([True, False], repeat=len(variables)):
        yield dict(zip(variables, combination))


def satisfiable(exp):
    """Tests whether the specified expression is satisfiable.

    An expression is satisfiable if there is a truth assignment to its
    variables that makes the expression evaluate to true.

    Args:
        exp: A Boolean expression.

    Returns:
        A truth assignment that makes the specified expression evaluate to
        true, or False in case there does not exist such an assignment.
        A truth assignment is represented as a dictionary mapping variable
        names to truth values.
    """

    for i in assignments(exp.variables):
        if exp.value(i):
            return i
    return False


def tautology(exp):
    """Tests whether the specified expression is a tautology.

    An expression is a tautology if it evaluates to true under all
    truth assignments to its variables.

    Args:
        exp: A Boolean expression.

    Returns:
        True if the specified expression is a tautology, False otherwise.
    """
    # TODO: Complete this function


def equivalent(exp1, exp2):
    """Tests whether the specified expressions are equivalent.

    Two expressions are equivalent if they have the same truth value under
    each truth assignment.

    Args:
        exp1: A Boolean expression.
        exp2: A Boolean expression.

    Returns:
        True if the specified expressions are equivalent, False otherwise.
    """

    for i in assignments(exp1.variables()):
        if exp1.value(i) != exp2.value(i):
            return False
    return True

def testEquivalent1():
    """Tests two expessions proven not to be equivalent

    Returns:
        False.
    """
    # Returns True
    p = Var('p')
    q = Var('q')
    r = Var('r')
    exp1 = Impl(Impl(p, q), r)
    exp2 = Conj(Disj(p, q), Disj(Nega(q), r))
    return equivalent(exp1, exp2)


def testEquivalent2():
    """Tests two expressions proven to be equivalent

    Returns:
        True.
    """
    p = Var('p')
    q = Var('q')

    exp1 = Impl(p, q)
    exp2 = Disj(Nega(p), q)
    return equivalent(exp1, exp2)


if __name__ == "__main__":
    print("Equivalent test 1")
    assert testEquivalent1() == False
    print("Equivalent test 2")
    assert testEquivalent2() == True
