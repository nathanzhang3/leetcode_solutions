class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
      
        for i in range(len(s)):
            for j in range(i+1):
                substr = s[j:j+len(s)-i]
                if substr == substr[::-1]:
                    return substr