class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 # assume buy on day zero (index)
        sell = 1 # assume sell on day one (index)
        max_profit = 0


        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
            else:
                buy = sell
            sell += 1

        return max_profit