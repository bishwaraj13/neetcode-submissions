# We want subarray that has maximum sum
# Subarray means contiguous

# So at each index i, I have choice to continue with previous subarray
# OR I could start a new subarray at i-th index
# max(solve(i-1)+nums[i], nums[i])

# But there's a catch.
# when we start at solve(5),
# we only check the best subarray sum that ends at solve(5)
# To check for best subarray sum, we need to check solve(i) for each i
# for i in range(len(nums)):
#     ans = max(ans, solve(i))

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i == 0:
                return nums[0]

            if i in memo:
                return memo[i]

            memo[i] = max(
                nums[i],
                nums[i] + solve(i - 1)
            )
            return memo[i]

        ans = float('-inf')

        for i in range(len(nums)):
            ans = max(ans, solve(i))

        return ans
        