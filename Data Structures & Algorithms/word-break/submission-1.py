# memo[i] stores whether the suffix s[i:] can be broken into
# valid dictionary words.
#
# Starting from index i, we try every possible ending position j.
# So s[i:j] is the current candidate word.
#
# Conceptually, at each position we have two choices:
#
# 1. Keep extending the current word:
#       s[i:j] -> s[i:j+1]
#
#    In this implementation, we don't need a recursive state for this.
#    The for-loop handles it by simply moving j forward.
#
# 2. If s[i:j] is a valid dictionary word, cut here and
#    check whether the remaining suffix s[j:] can also be segmented:
#
#       if s[i:j] in words and dfs(j):
#           memo[i] = True
#           return True
#
# Important: if s[i:j] is a valid word but dfs(j) returns False,
# we do NOT give up. We continue increasing j, because s[i:j]
# may be only a prefix of a larger valid word.
#
# Example:
#   s = "importantin"
#   words = {"import", "important", "in"}
#
# We first find "import", but dfs(6) fails on "antin".
# The loop then keeps extending j and later finds "important".
# dfs(9) succeeds because the remaining suffix is "in".
#
# If every possible j fails, then s[i:] cannot be segmented,
# so we store memo[i] = False.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}

        def dfs(i):
            # Reached the end successfully
            if i == len(s):
                return True

            # Same suffix already solved
            if i in memo:
                return memo[i]

            # Try every possible next word
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]

                if word in words and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)