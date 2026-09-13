class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        # If total sum is odd, we cannot split it into
        # two subsets with equal sums.
        if total % 2 != 0:
            return False

        target = total // 2

        # memo[(i, remaining)] tells us whether it's possible
        # to make 'remaining' using nums[i:]
        memo = {}

        def dfs(i, remaining):
            # We successfully found a subset whose sum is target
            if remaining == 0:
                return True

            # No more numbers left, or we exceeded the target
            if i == len(nums) or remaining < 0:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            # Choice 1: include nums[i]
            include = dfs(i + 1, remaining - nums[i])

            # Choice 2: do not include nums[i]
            exclude = dfs(i + 1, remaining)

            memo[(i, remaining)] = include or exclude
            return memo[(i, remaining)]

        return dfs(0, target)
        