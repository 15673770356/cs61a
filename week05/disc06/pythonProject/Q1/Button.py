LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class CapsLock:
    def __init__(self):
        self.pressed = 0

    def press(self):
        self.pressed += 1

class Button:
    """A button on a keyboard.

    >>> f = lambda c: print(c, end='')  # The end='' argument avoids going to a new line
    >>> k, e, y = Button('k', f), Button('e', f), Button('y', f)
    >>> s = e.press().press().press()
    eee
    >>> caps = Button.caps_lock
    >>> t = [x.press() for x in [k, e, y, caps, e, e, k, caps, e, y, e, caps, y, e, e]]
    keyEEKeyeYEE
    >>> u = Button('a', print).press().press().press()
    A
    A
    A
    """
    caps_lock = CapsLock()


    def __init__(self, letter, output):
        assert letter in LOWERCASE_LETTERS
        self.letter = letter
        self.output = output
        self.pressed = 0 # 被按下的次数

    def press(self):
        """Call output on letter (maybe uppercased), then return the button that was pressed."""
        self.pressed += 1  # 按压次数 ， 和 哪个不一样
        "*** YOUR CODE HERE ***"
        # 特殊情况
        if self.letter == 'caps' :
            Button.caps_lock.press()

        if Button.caps_lock.pressed % 2 == 1 :
            self.letter = self.letter.upper()
        else:
            self.letter = self.letter.lower()

    # 为什么可以重复按下按钮 ，因为除了显示结果之外，还会返回自身
        # 因为每次会返回一个实例  , 并且 加 1
        self.output(self.letter)
        return self








