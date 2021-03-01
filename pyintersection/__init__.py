"""
implemented :
geometric objects :
point2
line2
segment2

intersection functions :
ipoint2_line2
ilines2
ipoint2_segment2
iline2_segment2
isegments2
"""
from random import *
from collections import namedtuple
from math import inf
from fractions import Fraction


point2 = namedtuple("point2", ["x", "y"])


class line2():
    """ defined by a and b of the y = ax + b equation
        where a is the slope and b the y_intercept
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __contains__(self, other):
        """ Return True if other is fully contained in self, False otherwise
        """
        if isinstance(other, point2):
            return other.y == self.a * other.x + self.b
        elif isinstance(other, segment):
            return (other.a.y == self.a * other.a.x + self.b) and (other.b.y == self.a * other.b.x + self.b)
        else: raise NotImplementedError


class segment2():
    """ defined by 2 point2, a and b
    """
    def __init__(self, a, b):
        if isinstance(a, point2): self.a = a
        elif hasattr(a, '__iter__'): self.a = point2(*a)
        else: raise TypeError
        
        if isinstance(b, point2): self.b = b
        elif hasattr(b, '__iter__'): self.b = point2(*b)
        else: raise TypeError
        
    def __contains__(self, other):
        if isinstance(other, point2):
            if (other.y == self.slope() * other.x + self.y_intercept()) and \
            (other.x >= min(self.a.x, self.b.x) and other.x <= max(self.a.x, self.b.x)) and \
            (other.y >= min(self.a.y, self.b.y) and other.y <= max(self.a.y, self.b.y)): return True
            else: return False
        else: raise NotImplementedError

    def slope(self):
        """ if the line is vertical, the slope is considered infinite and
            return math.inf
        """
        x = self.b.x - self.a.x
        if x == 0: return inf
        y = self.b.y - self.a.y
        return y / x

    def y_intercept(self):
        #y  = ax + b
        #y  = b
        #b  = ax + b
        #ax = 0
        #x  = 0
        #p.y == l.slope() * p.x + b
        return self.a.y - self.a.x * self.slope()

    def line(self):
        return line2(self.slope(), self.y_intercept())


def ipoint2_line2(p, l): # 4
    """ return None if there is no intersection
        if there is return p
    """
    # y = ax + b
    if p.y == l.a * p.x + l.b: return p
    return None

def ilines2(l1, l2): # 4
    """ return None if there is no intersection
        if there is, can return :
        - a point2
        - a line2
    """

    if l1.a == l2.a:
        if l1.b == l2.b: return l1
        return None
    else:
        # y = ax + b
        # y = Ax + B
        # ax + b = Ax + B
        # ax - Ax = B - b
        # x(a - A) = B - b
        # x = (B - b)/(a - A)
        x = (l1.b - l2.b)/(l2.a - l1.a)
        y = l1.a * x + l1.b
        return point2(x, y)

def ipoint2_segment2(p, s): # 6
    """ return None if there is no intersection
        if there is return p
    """
    if p in s: return p
    return None

def iline2_segment2(l, s): # 6
    """ return None if there is no intersection
        if there is, can return :
        - a point2
        - a segment2
    """
    lines_intersection = ilines2(l, s.line())
    if lines_intersection is None: return None
    else:
        if isinstance(lines_intersection, point2):
            if (lines_intersection in l) and (lines_intersection in s):
                return lines_intersection
            return None
        elif isinstance(lines_intersection, line2):
            return s
        
def isegments2(s1, s2): # 8
    """ return None if there is no intersection
        if there is, can return :
        - a point2
        - a segment2
    """
    lines_intersection = ilines2(s1.line(), s2.line())
    if lines_intersection is None: return None
    else:
        if isinstance(lines_intersection, point2):
            if (lines_intersection in s1) and (lines_intersection in s2):
                return lines_intersection
            return None
        elif isinstance(lines_intersection, line2):
            # if the 2 lines are "merged", it can return :
            # None, a point, another segment
            a = None
            b = None
            if   s1.a in s2: a = s1.a
            elif s1.b in s2: a = s1.b
            if   s2.a in s1: b = s2.a
            elif s2.b in s1: b = s2.b
            if (a is None) and (b is None): return None
            elif a == b: return a
            else: return segment2(a, b)

if __name__ == "__main__":

    # isegments tests :
    a = point2(Fraction(1),Fraction(0))
    b = point2(Fraction(4),Fraction(3))

    c = point2(Fraction(1),Fraction(2))
    d = point2(Fraction(4),Fraction(1))

    j = segment2(a,b)
    k = segment2(c,d)

    expected = point2(x=Fraction(5, 2), y=Fraction(3, 2))

    assert isegments2(j,k) == expected, 'isegments2 is broken :/'













































