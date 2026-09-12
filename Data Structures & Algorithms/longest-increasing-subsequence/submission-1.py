class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def solve(i, previous_index):
            if i == n:
                return 0

            if (i, previous_index) in dp:
                return dp[(i, previous_index)]

            not_take = solve(i + 1, previous_index)

            take = 0
            if previous_index == -1 or nums[i] > nums[previous_index]:
                take = 1 + solve(i + 1, i)

            dp[(i, previous_index)] = max(take, not_take)
            return dp[(i, previous_index)]

        return solve(0, -1)