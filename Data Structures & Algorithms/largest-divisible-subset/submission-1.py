# Its one of the few problems where bottom up approach is intuitive and easier

# Few things that would help:
# small_number % big_number will always be 0,
# so it helps if we sort it, and then try to make chain.

# Second, if we have a, b, c, d
# and a%b==0 and b%c==0, then by transitivity a%c==0

# We initialize an array dp
# dp is same length as nums
# dp[i] stores length of longest subset till i-th index
# By default all of dp[i] will be initialized as 1.
# Because each element is divisible by itself, so at least
# each index is a chain of length 1

# We also need parents array.
# parents[i] stores previous index in the best chain
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = [-1] * n

        best_len = 1
        best_end = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i

        # Reconstruct the subarray answer - O(n)
        ans = []
        curr = best_end

        while curr != -1:
            ans.append(nums[curr])
            curr = parent[curr]

        ans.reverse()
        return ans

        