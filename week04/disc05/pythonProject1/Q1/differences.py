def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    iterator = iter(t)
    previous = next(iterator)
# previous 只需要使用一个就可以了 
    for current in iterator:
        yield current - previous
        previous = current


print(list(differences(iter([5, 2, -100, 103]))))