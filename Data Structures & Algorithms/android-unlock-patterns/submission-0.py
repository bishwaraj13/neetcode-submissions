# We need to make skip matrix
# E.g., to go from 1 to 3, we need to pass through 2

# we need visited array to track which nodes have been visited already


class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:

        # skip[a][b] = x
        # means a -> b move requires x to be already visited
        skip = [[0] * 10 for _ in range(10)]

        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8

        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[2][8] = skip[8][2] = 5
        skip[4][6] = skip[6][4] = 5

        visited = [False] * 10

        def dfs(cur, remaining):
            # required length is finished
            if remaining == 0:
                return 1

            count = 0

            visited[cur] = True

            for nxt in range(1, 10):

                if visited[nxt]:
                    continue

                middle = skip[cur][nxt]

                # move is valid if:
                # 1. there are no middle dots
                # OR
                # 2. middle dot is already visited
                if middle == 0 or visited[middle]:
                    count += dfs(nxt, remaining - 1)

            # We need to backtrack
            visited[cur] = False

            return count

        ans = 0

        # for every length from m to n
        for length in range(m, n + 1):
            # we explore all the 9 number as starting point
            for start in range(1, 10):
                ans += dfs(start, length - 1)

        return ans