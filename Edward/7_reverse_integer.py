class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = cmp(x, 0)
        rev = sign * int(str(abs(x))[::-1])
        if (rev > (-2)**31) and (rev < 2**31-1):
            return rev
        else:
            return 0