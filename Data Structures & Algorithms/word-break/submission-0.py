# we maintain memo
# memo[i] is to find any word that starts at i and is present in dictionary
# so basically we iterate j from i+1 to end of string,
# and look for word in dictionary
# Say we found s[i:j] as a word in dictionary, then we do
# if word in words and dfs(j):
#     memo[i] = True
#     return True

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