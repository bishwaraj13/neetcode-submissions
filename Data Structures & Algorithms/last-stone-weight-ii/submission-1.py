from typing import List


# Approach:
# - Instead of simulating all possible smash orders, split the stones
#   conceptually into two groups.
# - The final remaining stone weight is the absolute difference between
#   the sums of those two groups.
# - For every stone, recursively choose to:
#       1. Add its weight to the current difference.
#       2. Subtract its weight from the current difference.
# - When all stones are processed, return abs(diff).
# - Use a dictionary to memoize each (index, diff) state so repeated
#   subproblems are not recomputed.
#
# Time Complexity:
# - O(n * total_sum)
#
# Space Complexity:
# - O(n * total_sum)


class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}

        def dfs(i, diff):
            if i == len(stones):
                return abs(diff)

            if (i, diff) in memo:
                return memo[(i, diff)]

            add = dfs(i + 1, diff + stones[i])
            subtract = dfs(i + 1, diff - stones[i])

            memo[(i, diff)] = min(add, subtract)

            return memo[(i, diff)]

        return dfs(0, 0)