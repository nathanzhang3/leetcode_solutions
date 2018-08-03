class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()
        char_lst = [char for char in s if char.isalpha() or char.isdigit()]
        
        return char_lst == char_lst[::-1]