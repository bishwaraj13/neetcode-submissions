class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(target):
            # No more sum is left to make.
            if target == 0:
                return 0

            # Return the answer if we already solved this target.
            if target in memo:
                return memo[target]

            # Worst case:
            # target = 1^2 + 1^2 + ... target times
            res = target

            # Start from the largest possible perfect square.
            i = int(target ** 0.5)

            while i >= 1:
                square = i * i

                # Choose this square once,
                # then recursively solve the remaining target.
                current = 1 + dfs(target - square)

                # Keep the minimum among all possible choices.
                res = min(res, current)

                i -= 1

            memo[target] = res
            return res

        return dfs(n)