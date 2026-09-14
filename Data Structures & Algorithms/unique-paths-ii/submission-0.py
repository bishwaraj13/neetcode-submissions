class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = {}

        def solve(r, c):
            # grid ke bahar
            if r >= rows or c >= cols:
                return 0

            # obstacle
            if obstacleGrid[r][c] == 1:
                return 0

            # destination mil gaya
            if r == rows - 1 and c == cols - 1:
                return 1

            # already calculated
            if (r, c) in dp:
                return dp[(r, c)]

            down = solve(r + 1, c)
            right = solve(r, c + 1)

            dp[(r, c)] = down + right
            return dp[(r, c)]

        return solve(0, 0)