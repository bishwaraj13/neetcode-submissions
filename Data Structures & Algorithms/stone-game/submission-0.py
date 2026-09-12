from typing import List

class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        # ------------------------------------------------------------
        # KEY IDEA
        # ------------------------------------------------------------
        #
        # Our objective function is:
        #
        #       Alice's score - Bob's score
        #
        # We want to know the final value of this objective
        # when both players play optimally.
        #
        #
        # Alice's goal:
        #   MAXIMIZE our objective
        #
        #       Alice - Bob
        #
        # A larger value is better for Alice.
        #
        #
        # Bob's goal:
        #   MINIMIZE our objective
        #
        #       Alice - Bob
        #
        # A smaller value is better for Bob.
        #
        #
        # Example:
        #
        # If the possible final objective values are:
        #
        #       5 and 2
        #
        # Alice chooses 5 because she is maximizing.
        #
        #
        # If the possible final objective values are:
        #
        #       4 and -2
        #
        # Bob chooses -2 because he is minimizing.
        #
        #
        # ------------------------------------------------------------
        # WHY DO WE ADD FOR ALICE AND SUBTRACT FOR BOB?
        # ------------------------------------------------------------
        #
        # Our objective is:
        #
        #       Alice - Bob
        #
        # So if Alice gets a pile:
        #
        #       +pile
        #
        # because Alice's side of the objective increases.
        #
        # If Bob gets a pile:
        #
        #       -pile
        #
        # because Bob's score is being subtracted in our objective.
        #
        #
        # Therefore:
        #
        # Alice's turn -> +pile -> maximize objective
        # Bob's turn   -> -pile -> minimize objective
        #
        #
        # Finally:
        #
        # If Alice - Bob > 0 -> Alice wins
        # If Alice - Bob < 0 -> Bob wins
        #
        # ------------------------------------------------------------

        memo = {}

        def solve(left, right, alice_turn):

            # No piles left, so this contributes 0
            # to our objective.
            if left > right:
                return 0

            key = (left, right, alice_turn)

            if key in memo:
                return memo[key]

            if alice_turn:

                # Alice takes the left pile.
                # Add it because our objective is Alice - Bob.
                take_left = (
                    piles[left]
                    + solve(left + 1, right, False)
                )

                # Alice takes the right pile.
                take_right = (
                    piles[right]
                    + solve(left, right - 1, False)
                )

                # Alice wants to MAXIMIZE our objective.
                memo[key] = max(take_left, take_right)

            else:

                # Bob takes the left pile.
                # Subtract it because our objective is Alice - Bob.
                take_left = (
                    -piles[left]
                    + solve(left + 1, right, True)
                )

                # Bob takes the right pile.
                take_right = (
                    -piles[right]
                    + solve(left, right - 1, True)
                )

                # Bob wants to MINIMIZE our objective.
                memo[key] = min(take_left, take_right)

            return memo[key]

        # Alice wins if our final objective is positive.
        return solve(0, len(piles) - 1, True) > 0