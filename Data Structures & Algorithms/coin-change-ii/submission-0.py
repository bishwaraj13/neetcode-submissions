# This is similar to Unbounded Knapsack
class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, remaining):
            if remaining == 0:
                return 1

            if i == len(coins):
                return 0

            state = (i, remaining)

            if state in memo:
                return memo[state]

            # Don't use coins[i]
            skip = dfs(i + 1, remaining)

            # Use coins[i]
            take = 0

            if coins[i] <= remaining:
                take = dfs(i, remaining - coins[i])

            memo[state] = skip + take
            return memo[state]

        return dfs(0, amount)