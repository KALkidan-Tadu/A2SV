class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        currAmount = float("-inf")
        profit = 0
        n = len(prices)

        for i in range(n):
            currAmount = max(currAmount, profit - prices[i])
            profit = max(profit, currAmount+ prices[i] - fee)
        
        return profit
