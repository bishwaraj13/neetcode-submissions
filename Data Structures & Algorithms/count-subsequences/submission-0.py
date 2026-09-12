class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def solve(i, j):
            # Successfully formed t
            if j == len(t):
                return 1

            # s is finished but t is not
            if i == len(s):
                return 0

            # Already calculated
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                # Take + Skip
                memo[(i, j)] = solve(i + 1, j + 1) + solve(i + 1, j)
            else:
                # Skip
                memo[(i, j)] = solve(i + 1, j)

            return memo[(i, j)]

        return solve(0, 0)