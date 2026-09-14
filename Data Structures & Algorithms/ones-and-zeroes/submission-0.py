# This is exactly like 10 Knapsack, except we have two capacities of 1s and 0s
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []

        # Make the count of zeroes and ones in parsable format
        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")
            counts.append((zeros, ones))

        memo = {}

        def dfs(i, zeros_left, ones_left):
            # Base case: no strings left
            if i == len(strs):
                return 0

            state = (i, zeros_left, ones_left)

            # Reuse an already solved state
            if state in memo:
                return memo[state]

            z, o = counts[i]

            # Option 1: skip current string
            skip = dfs(i + 1, zeros_left, ones_left)

            # Option 2: take current string, if it fits
            take = 0
            if z <= zeros_left and o <= ones_left:
                take = 1 + dfs(
                    i + 1,
                    zeros_left - z,
                    ones_left - o
                )

            memo[state] = max(skip, take)
            return memo[state]

        return dfs(0, m, n)