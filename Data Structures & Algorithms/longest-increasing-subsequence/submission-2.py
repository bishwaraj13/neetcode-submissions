# Recursion and Top-Down is very intuitive,
# but unfortnately binary search approach is more optimized
# and will be useful in other sorting problems.

# The Recursion Problem that we dont use is here:
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = {}

#         def solve(i, previous_index):
#             if i == n:
#                 return 0

#             if (i, previous_index) in dp:
#                 return dp[(i, previous_index)]

#             not_take = solve(i + 1, previous_index)

#             take = 0
#             if previous_index == -1 or nums[i] > nums[previous_index]:
#                 take = 1 + solve(i + 1, i)

#             dp[(i, previous_index)] = max(take, not_take)
#             return dp[(i, previous_index)]

#         return solve(0, -1)

from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        def lower_bound(tails, target):
            left = 0
            right = len(tails) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if tails[mid] >= target:
                    # mid could be the answer,
                    # but there may be an earlier valid position.
                    right = mid - 1
                else:
                    # tails[mid] < target,
                    # so target must go somewhere to the right.
                    left = mid + 1

            # left is the first index where tails[left] >= target
            return left

        # tails[i] stores the smallest possible ending value
        # of an increasing subsequence of length i + 1.
        #
        # Example:
        # tails = [2, 3, 7]
        #
        # means:
        # length 1 subsequence can end at 2
        # length 2 subsequence can end at 3
        # length 3 subsequence can end at 7
        tails = []

        for num in nums:

            # Find where this number should go.
            pos = lower_bound(tails, num)

            if pos == len(tails):
                # num is larger than every value in tails.
                #
                # So we can extend the longest increasing subsequence.
                tails.append(num)

            else:
                # We found an existing subsequence of this length,
                # but num gives us a smaller/better ending value.
                #
                # We replace instead of inserting.
                # The length of tails does NOT change here.
                tails[pos] = num

        # tails itself is not necessarily the actual LIS.
        # But its length is always the LIS length.
        return len(tails)