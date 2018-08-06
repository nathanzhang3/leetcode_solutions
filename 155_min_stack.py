class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack == []:
            self.stack.append((x, x))
        else:
            last_min = self.stack[-1][1]
            self.stack.append((x, min(x, last_min)))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]
