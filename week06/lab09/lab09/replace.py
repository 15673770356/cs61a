def gcd (a , b ) : 
    """
    >>>a = gcd (5,3)
    >>>a 
    1 
    >>>b = gcd (4,2)
    >>>b 
    2
    """
    c =  min(a , b )
    d =  max(a , b )
    if d % c == 0 : 
        return c 
    else :
        return gcd(c , d % c )


a = gcd (4,2)
print(a)