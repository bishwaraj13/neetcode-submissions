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