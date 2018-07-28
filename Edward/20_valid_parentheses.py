class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_dict = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in s_dict.values():
                stack.append(i)
            if i in s_dict.keys():
                if (not stack) or (stack[-1] != s_dict[i]):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0