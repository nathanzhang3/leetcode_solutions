class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 0) or ("" in strs):
            return ""
        num = 0
        for i, val in enumerate(zip(*strs)):
            if val.count(val[0]) != len(val):
                return strs[0][:i]
            else:
                num = i
        return strs[0][:num+1]