class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        profit = 0
        
        # for i in range(n-1):
        #     for j in range(i+1 , n):
        #         profit = max(profit , (prices[j] - prices[i]))

        # return profit

        min_price = float('inf')
        for price in prices:
            min_price = min(min_price , price)
            profit = max(profit , price - min_price)

        return profit
            





