


def invert(num):
    try:
        return 1 / num
    except ZeroDivisionError :
        return  0

print(invert(0))