class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time: O(n)
        space: O(1)
        """
        buy = float('Inf')
        max_profit = 0
        for price in prices:
            if buy > price: buy = price
            profit = price - buy
            max_profit = max(profit, max_profit)
        return max_profit 