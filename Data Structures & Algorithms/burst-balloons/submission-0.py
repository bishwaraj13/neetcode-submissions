from typing import List

class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}

        def solve(left, right):
            # no balloon between left and right
            if right - left == 1:
                return 0

            if (left, right) in memo:
                return memo[(left, right)]

            best = 0

            # try every balloon as the LAST balloon
            # to burst between left and right
            for k in range(left + 1, right):

                coins = (
                    solve(left, k)
                    + nums[left] * nums[k] * nums[right]
                    + solve(k, right)
                )

                best = max(best, coins)

            memo[(left, right)] = best
            return best

        return solve(0, len(nums) - 1)