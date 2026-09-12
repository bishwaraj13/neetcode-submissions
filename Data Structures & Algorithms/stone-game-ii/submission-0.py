from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        @lru_cache(None)
        def solve(i, M, alice_turn):
            if i >= n:
                return 0

            max_x = min(2 * M, n - i)

            if alice_turn:
                best = 0
                stones_taken = 0

                for X in range(1, max_x + 1):
                    stones_taken += piles[i + X - 1]

                    result = stones_taken + solve(
                        i + X,
                        max(M, X),
                        False
                    )

                    best = max(best, result)

                return best

            else:
                best = float("inf")

                for X in range(1, max_x + 1):
                    result = solve(
                        i + X,
                        max(M, X),
                        True
                    )

                    best = min(best, result)

                return best

        return solve(0, 1, True)