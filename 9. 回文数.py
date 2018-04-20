def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 0:
        newx = x
    else:
        return False

    res = 0

    while newx != 0:
        res *= 10
        res += newx % 10
        newx //= 10

    if res == x:
        return True
    else:
        return False

print(reverse(-121))