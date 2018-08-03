class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0: return 0
        
        
        sign = -1 if s[0] == '-' else 1
        if s[0] in ['+','-']: s = s[1:]
        int_sum, i = 0, 0
        while i < len(s) and s[i].isdigit():
            int_sum = int_sum * 10 + int(s[i])
            i += 1
        
        return max(-2**31, min(2**31-1, sign * int_sum))