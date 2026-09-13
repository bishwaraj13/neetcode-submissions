class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # memo[(i, current_sum)] stores:
        # number of ways to reach target starting from index i
        # when our current sum is current_sum
        memo = {}

        def dfs(i, current_sum):

            # Base case:
            # We have assigned + or - to every number
            if i == len(nums):

                # If final sum equals target,
                # we found one valid way
                if current_sum == target:
                    return 1

                return 0

            # If we already solved this state,
            # return the stored result
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            # Choice 1:
            # Put a '+' before nums[i]
            add = dfs(i + 1, current_sum + nums[i])

            # Choice 2:
            # Put a '-' before nums[i]
            subtract = dfs(i + 1, current_sum - nums[i])

            # Total number of ways from this state
            memo[(i, current_sum)] = add + subtract

            return memo[(i, current_sum)]

        # Start at index 0 with sum = 0
        return dfs(0, 0)
