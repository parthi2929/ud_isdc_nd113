def a_or_b_but_not_both(set_a, set_b):
    """Returns a set which contains any element that is 
    a member of set_a OR a member of set_b but NOT a member
    of both."""
    union = set_a.union(set_b)
    intersection = set_a.intersection(set_b)
    return union-intersection

# Initializing two sets

odds   = set([1,3,5,7,9])
primes = set([2,3,5,7])

# testing code
assert a_or_b_but_not_both(odds, primes) == set([9,1,2])
print("Nice job! Your function works correctly!")