class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def tree_value(self):
        # 将一棵树的所有节点的值汇成一张list
        value = [self.label]
        for b in self.branches:
            value.extend(b.tree_value())
        return value

    def bst_min(self):
        """
        返回树的最小值
        """
        value = self.tree_value()
        return min(value)

    def bst_max(self):
        """
        返回树的最大值
        """
        value = self.tree_value()
        return max(value)


