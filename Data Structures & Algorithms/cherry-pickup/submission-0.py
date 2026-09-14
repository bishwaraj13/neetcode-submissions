# Instead of Traveller A going downward and Traveller B travelling in return trip,
# we do both travelling downward together simultaneously
class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Used for invalid paths.
        # We want invalid branches to never win inside max().
        NEG = float("-inf")

        # Manual memoization:
        # key   = (r1, c1, r2)
        # value = maximum cherries collectable from this state onward
        memo = {}

        def dfs(r1, c1, r2):
            """
            Traveler A is at (r1, c1)

            Traveler B is at (r2, c2)

            Both travelers have taken the same number of moves.

            Therefore:
                r1 + c1 = r2 + c2

            So:
                c2 = r1 + c1 - r2

            That is why we only need 3 variables in our state.
            """

            c2 = r1 + c1 - r2

            # ---------------------------------------------------------
            # 1. INVALID STATE
            # ---------------------------------------------------------
            # If either traveler goes outside the grid,
            # this particular combination of paths is invalid.
            #
            # Important:
            # We are NOT cancelling A's move globally or B's move globally.
            # We are only rejecting THIS specific pairing of their paths.
            # ---------------------------------------------------------
            if (
                r1 >= n or
                c1 >= n or
                r2 >= n or
                c2 >= n or
                c2 < 0
            ):
                return NEG

            # If either traveler lands on a thorn,
            # this pair of paths is invalid.
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return NEG

            # ---------------------------------------------------------
            # 2. MEMOIZATION
            # ---------------------------------------------------------
            state = (r1, c1, r2)

            if state in memo:
                return memo[state]

            # ---------------------------------------------------------
            # 3. BASE CASE
            # ---------------------------------------------------------
            # If A reaches the destination and B is still in-bounds,
            # then B must also be at the destination.
            #
            # Why?
            # Both have taken the same number of moves.
            # Destination requires exactly 2*n - 2 moves.
            # ---------------------------------------------------------
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            # ---------------------------------------------------------
            # 4. COLLECT CHERRIES AT CURRENT POSITIONS
            # ---------------------------------------------------------
            cherries = grid[r1][c1]

            # If both travelers are on different cells,
            # collect B's cherry too.
            #
            # If they are on the same cell,
            # that cherry must be counted only once.
            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]

            # ---------------------------------------------------------
            # 5. TRY ALL 4 MOVE COMBINATIONS
            # ---------------------------------------------------------
            #
            # A can move:
            #   Down  -> r1 + 1
            #   Right -> c1 + 1
            #
            # B can move:
            #   Down  -> r2 + 1
            #   Right -> r2 stays same
            #
            # Remember:
            # We don't explicitly pass c2 because it is reconstructed.
            # ---------------------------------------------------------

            both_down = dfs(
                r1 + 1,
                c1,
                r2 + 1
            )

            a_down_b_right = dfs(
                r1 + 1,
                c1,
                r2
            )

            a_right_b_down = dfs(
                r1,
                c1 + 1,
                r2 + 1
            )

            both_right = dfs(
                r1,
                c1 + 1,
                r2
            )

            best_next = max(
                both_down,
                a_down_b_right,
                a_right_b_down,
                both_right
            )

            # If all future combinations are invalid,
            # then this current state is also invalid.
            if best_next == NEG:
                memo[state] = NEG
                return NEG

            # Current cherries + best possible future result.
            memo[state] = cherries + best_next

            return memo[state]

        # Both travelers start from (0, 0).
        #
        # A = (0, 0)
        # B = (0, 0)
        #
        # We only pass r2 = 0 because c2 will also become 0.
        answer = dfs(0, 0, 0)

        # If no valid complete path exists,
        # answer will effectively be invalid.
        return max(0, answer)