class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def match(i, j):

            # already solved this state
            if (i, j) in memo:
                return memo[(i, j)]

            # both string and pattern are finished
            if i == len(s) and j == len(p):
                return True

            # pattern finished, but string is not
            if j == len(p):
                return False

            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == '.')
            )

            # next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                skip = match(i, j + 2)

                use = (
                    first_match
                    and match(i + 1, j)
                )

                result = skip or use

            else:
                result = (
                    first_match
                    and match(i + 1, j + 1)
                )

            memo[(i, j)] = result
            return result

        return match(0, 0)