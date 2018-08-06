class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        else:
            dailyChg = [b-a for a, b in zip(prices[:-1], prices[1:])]

            for i in range(1, len(dailyChg)):
                if dailyChg[i-1] > 0:
                    dailyChg[i] += dailyChg[i-1]

            return max(dailyChg + [0])