from operator import mul , add

def reduce (func , lst , start) :
    """
    reduce(mul , [1 , 2 , 3 ,4 ] , 2 )
    >>>64
    """
    for x in lst :
        start = func(start , x )
    return start

print(reduce(mul , [1 , 2 , 3 ,4 ] , 2 ))