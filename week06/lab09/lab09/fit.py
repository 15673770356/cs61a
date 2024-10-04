
def fit(total, n):
    """
    判断是否能将total分解成n个不同的完美平方数的和。
    
    >>> fit(10, 2)
    True
    >>> fit(9, 1)
    True
    >>> fit(25, 2)
    True
    """
    # 设置递归深度上限
    sys.setrecursionlimit(3000)

    memo = {}

    def fith(total, n, k):
        # 如果已经计算过该状态，则直接返回结果
        if (total, n, k) in memo:
            return memo[(total, n, k)]

        if total == 0 and n == 0:
            return True
        if total < 0 or n < 0 or k * k > total:
            return False

        # 使用当前的平方数k**2
        use_current = fith(total - k**2, n - 1, k + 1)
        # 不使用当前的平方数k**2
        skip_current = fith(total, n, k + 1)

        result = use_current or skip_current
        # 缓存结果以备后续使用
        memo[(total, n, k)] = result

        return result

    return fith(total, n, 1)

# 测试
if __name__ == "__main__":
    import doctest
    doctest.testmod()