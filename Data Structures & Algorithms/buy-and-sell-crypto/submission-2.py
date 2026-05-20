class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            mp = max(profit, mp, 0)
            if prices[buy] > prices[sell]:
                buy = sell
            sell += 1
        return mp

        