from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def solve(i, alice_turn):
            if i >= n:
                return 0

            if (i, alice_turn) in memo:
                return memo[(i, alice_turn)]

            if alice_turn:
                best = float("-inf")
                stones_taken = 0

                for x in range(1, 4):
                    if i + x > n:
                        break

                    stones_taken += stoneValue[i + x - 1]

                    result = stones_taken + solve(i + x, False)
                    best = max(best, result)

            else:
                best = float("inf")

                for x in range(1, 4):
                    if i + x > n:
                        break

                    result = solve(i + x, True)
                    best = min(best, result)

            memo[(i, alice_turn)] = best
            return best

        alice_score = solve(0, True)

        total_score = sum(stoneValue)
        bob_score = total_score - alice_score

        if alice_score > bob_score:
            return "Alice"
        elif alice_score < bob_score:
            return "Bob"
        else:
            return "Tie"