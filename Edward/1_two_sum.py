def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = (1, -1)[x < 0]
    print sign
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2 ** 31) - 1 < rst < 2 ** 31 else 0

a = reverse(123)
print a

a = [1, -1][90 < 0]
print a

b = cmp(90, 0)
c = cmp(-85, 0)
print b, c