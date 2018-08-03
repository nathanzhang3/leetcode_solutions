class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        dailyChg = [p1 - p2 for p1, p2 in zip(prices[1:], prices[:-1])]
        
        return sum([posChg for posChg in dailyChg if posChg > 0])
        