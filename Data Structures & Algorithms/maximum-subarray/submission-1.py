# We want subarray that has maximum sum
# Subarray means contiguous

# So at each index i, I have choice to continue with previous subarray
# OR I could start a new subarray at i-th index
class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
        