class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rows = [[1]]

        for i in range(1, numRows):
            rows += [list(map(lambda x, y: x + y, rows[-1] + [0], [0] + rows[-1]))]
            
        return rows[:numRows]