class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        elif len(s) % 2 == 1:
            return False
        else:
            p_pairs = {'(':')',
                       '[':']',
                       '{':'}'}
            
            stored = []

            while len(s) > 0:
                if s[0] in p_pairs.keys():
                    stored.append(s[0])
                    s = s[1:]
                    if s == '':
                        return False
                elif len(stored) == 0:
                    return False
                elif s[0] == p_pairs[stored[-1]]:
                    s = s[1:]
                    stored.pop()
                else:
                    return False
                
            return True