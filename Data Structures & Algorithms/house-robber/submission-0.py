# Top Down
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         memo = [-1] * len(nums)

#         def dfs(i):
#             if i < 0:
#                 return 0
#             if memo[i] != -1:
#                 return memo[i]

#             memo[i] = max(dfs(i - 1), nums[i] + dfs(i - 2))
#             return memo[i]

#         return dfs(len(nums) - 1)

# Bottom Up
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            skip = dp[i - 1] if i - 1 >= 0 else 0
            rob = nums[i] + (dp[i - 2] if i - 2 >= 0 else 0)
            dp[i] = max(skip, rob)

        return dp[len(nums) - 1]