class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0 
        buy = 0
        max_profit = 0

        for i in range(len(prices)):
            profit = prices[i] - prices[buy] 

            if prices[i] < prices[buy]:
                buy = i
                continue

            if profit > max_profit: 
                max_profit = profit
        return max_profit