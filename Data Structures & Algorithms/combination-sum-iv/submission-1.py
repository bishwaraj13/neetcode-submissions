# In the below code, we don't use (i, remaining) as states like Unbounded Knapsack
# because we want both combinations like (1, 2) and (2, 1) {more like different permutations}
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(remaining):

            # If remaining becomes 0,
            # we found one valid way
            if remaining == 0:
                return 1

            # If already calculated, return stored answer
            if remaining in memo:
                return memo[remaining]

            ways = 0

            # Try every number as the next number
            for num in nums:
                if remaining - num >= 0:
                    ways += dfs(remaining - num)

            memo[remaining] = ways

            return ways

        return dfs(target)