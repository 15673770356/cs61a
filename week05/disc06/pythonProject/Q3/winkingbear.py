from eye import *

class WinkingBear(Bear):
    """A bear whose left eye is different from its right eye.

    >>> WinkingBear().print()
    ? -o0?
    """
    def __init__(self):
        "*** YOUR CODE HERE ***"
        self.num  =  0
        self.nose_and_mouth = 'o'

    def next_eye(self):
        "*** YOUR CODE HERE ***"
        if self.num  % 2 == 0 :
            self.num += 1
            return Eye(True)
        else:
            self.num +=1
            return Eye(False)


