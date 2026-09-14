# Solve House Robber original problem.
# Then run it twice
# Case 1: house_robber(0, n-2)
# Case 2: house_robber(1, n-1)
# return max(case1, case2)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def helper(start, end):
            dp = [0] * n

            for i in range(start, end + 1):
                skip = dp[i - 1] if i - 1 >= start else 0
                rob = nums[i] + (dp[i - 2] if i - 2 >= start else 0)

                dp[i] = max(skip, rob)

            return dp[end]

        # Case 1: last house ignore
        case1 = helper(0, n - 2)

        # Case 2: first house ignore
        case2 = helper(1, n - 1)

        return max(case1, case2)