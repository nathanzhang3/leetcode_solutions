class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0 or len(min(strs, key=len)) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            for i in range(len(min(strs, key=len))):
                substrs = [s[:i+1] for s in strs]
                if len(set(substrs)) > 1:
                    return strs[0][:i]
            return min(strs, key=len)