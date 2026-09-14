class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[-1] * 2 for _ in range(n)]

        def solve(day, can_buy):
            # Base case
            if day == n:
                return 0

            # Already calculated
            if dp[day][can_buy] != -1:
                return dp[day][can_buy]

            if can_buy:
                # Option 1: Buy today
                buy = -prices[day] + solve(day + 1, 0)

                # Option 2: Skip today
                skip = solve(day + 1, 1)

                dp[day][can_buy] = max(buy, skip)

            else:
                # Option 1: Sell today
                sell = prices[day] + solve(day + 1, 1)

                # Option 2: Keep holding
                hold = solve(day + 1, 0)

                dp[day][can_buy] = max(sell, hold)

            return dp[day][can_buy]

        return solve(0, 1)