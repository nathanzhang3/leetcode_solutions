# 56ms
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)

        if x_str[0]=='-':
            x_str_r = x_str[0]+x_str[1:][::-1]
        else:
            x_str_r = x_str[::-1]

        x_r = int(x_str_r)

        if -2**31 <= x_r <= 2**31-1:
            return x_r
        else:
            return 0
