class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i] = maximum profit we can make from day 0 to day i
        dp = [0] * n

        # Lowest price seen so far
        min_price = prices[0]

        # Start from day 1 because profit on day 0 is always 0
        for i in range(1, n):
            min_price = min(min_price, prices[i])

            profit_if_we_sell_today = prices[i] - min_price

            # Either keep the previous best profit
            # or sell today using the cheapest price seen so far
            dp[i] = max(dp[i - 1], profit_if_we_sell_today)

        return dp[n - 1]