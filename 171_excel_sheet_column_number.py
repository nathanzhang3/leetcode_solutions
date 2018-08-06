class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        reverse_s = s[::-1]
        sum = 0
        for power, char in enumerate(reverse_s):
            sum += (ord(char) - ord('A') + 1) * (26 ** power)
            
        return sum