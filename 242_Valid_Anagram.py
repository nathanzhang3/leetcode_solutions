class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if self.str_to_dict(s) == self.str_to_dict(t):
            return True
        else:
            return False
        
    def str_to_dict(self, s):
        char_dict = dict()
        for char in s:
            if char in char_dict.keys():
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        return char_dict
