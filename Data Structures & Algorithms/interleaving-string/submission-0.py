class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # If total lengths don't match, s3 cannot be an interleaving
        if len(s1) + len(s2) != len(s3):
            return False

        # memo[(i, j)] stores whether s3 can be formed
        # using s1[i:] and s2[j:]
        memo = {}

        def dfs(i, j):

            # If we already solved this state, return the saved answer
            if (i, j) in memo:
                return memo[(i, j)]

            # If we have used all characters from both s1 and s2,
            # then we successfully formed all of s3
            if i == len(s1) and j == len(s2):
                return True

            # Number of characters already used from s1 and s2
            # tells us the current index in s3
            k = i + j

            # Option 1:
            # Try taking the next character from s1
            option1 = False

            if i < len(s1) and s1[i] == s3[k]:
                option1 = dfs(i + 1, j)

            # Option 2:
            # Try taking the next character from s2
            option2 = False

            if j < len(s2) and s2[j] == s3[k]:
                option2 = dfs(i, j + 1)

            # If either path works, this state is valid
            memo[(i, j)] = option1 or option2

            return memo[(i, j)]

        # Start with index 0 in both s1 and s2
        return dfs(0, 0)
        