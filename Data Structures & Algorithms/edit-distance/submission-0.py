class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        memo = {}

        # dfs(i, j) = minimum edit distance needed
        # to convert word1[:i] into word2[:j]
        def dfs(i, j):

            # If word1 is empty, we must insert all j characters
            if i == 0:
                return j

            # If word2 is empty, we must delete all i characters
            if j == 0:
                return i

            # Return already-computed answer
            if (i, j) in memo:
                return memo[(i, j)]

            # Last characters already match
            # No operation needed, just move both pointers back
            if word1[i - 1] == word2[j - 1]:
                memo[(i, j)] = dfs(i - 1, j - 1)

            else:
                # Insert word2[j - 1] into word1
                # word1 still has i characters to process,
                # but word2 now has one fewer character to match
                insert = dfs(i, j - 1)

                # Delete word1[i - 1]
                # word1 now has one fewer character to process
                delete = dfs(i - 1, j)

                # Replace word1[i - 1] with word2[j - 1]
                # both characters are now handled
                replace = dfs(i - 1, j - 1)

                memo[(i, j)] = 1 + min(insert, delete, replace)

            return memo[(i, j)]

        return dfs(m, n)