class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        max_profit = 0
        min_price = float(inf)
        for x in range(N):
            min_price = min(min_price, prices[x])
            max_profit = max(max_profit, prices[x]-min_price)
        return max_profit 
