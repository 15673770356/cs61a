
def divide(a, b ) :
    try :
        ans = a / b
    except ZeroDivisionError  as e :
        print(type(e))
        ans = 0
    return  ans

print(divide(2 , 3)