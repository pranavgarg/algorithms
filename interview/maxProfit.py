class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = -1
        if not prices:
            return 0
        l = len(prices)
        for idx in range(l - 1):
            buy = prices[idx]
            for upidx in range(idx + 1, l):
                sell = prices[upidx]
                diff = sell - buy
                if diff >= 0:
                    max_profit = max(max_profit, diff)
        return max_profit


a = Solution()
print a.maxProfit([7,1,5,3,6,4])