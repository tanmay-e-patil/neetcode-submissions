class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        lowest = float('inf')
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            profit = max(profit, prices[i] - lowest)

        
        return profit

        # buyPrice = prices[0]
        # sellPrice = prices[1]

        # if buyPrice < sellPrice:
        #     profit = sellPrice - buyPrice
        #     max_pr

        