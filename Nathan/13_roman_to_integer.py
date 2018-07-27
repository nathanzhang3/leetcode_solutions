class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = {'M':1000,
                  'D':500,
                  'C':100,
                  'L':50,
                  'X':10,
                  'V':5,
                  'I':1}
        
        added = 0
        skip = False
        
        for k, v in enumerate(s):
            if not skip:
                if k < len(s)-1:
                    if romans[v] < romans[s[k+1]]:
                        added += romans[s[k+1]] - romans[v]
                        skip = True
                    else:
                        added += romans[v]
                else:
                    added += romans[v]
            else:
                skip = False
                
        return added