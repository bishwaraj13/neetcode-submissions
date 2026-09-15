# This is Top-Down Approach
# I havec converted the same code to Bottom-Up below
# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         memo = {}

#         def solve(i, j):
#             if j == len(str2):
#                 return str1[i:]

#             if i == len(str1):
#                 return str2[j:]

#             if (i, j) in memo:
#                 return memo[(i, j)]

#             if str1[i] == str2[j]:
#                 memo[(i, j)] = str1[i] + solve(i+1, j+1)
#                 return memo[(i, j)]
            
#             case1 = str1[i] + solve(i+1, j)
#             case2 = str2[j] + solve(i, j+1)

#             if len(case1) > len(case2):
#                 memo[(i, j)] = case2
#             else:
#                 memo[(i, j)] = case1
            
#             return memo[(i, j)]

#         return solve(0, 0)

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        # Base cases
        for i in range(m + 1):
            dp[i][n] = str1[i:]
        for j in range(n + 1):
            dp[m][j] = str2[j:]
        # Fill bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = str1[i] + dp[i + 1][j + 1]
                else:
                    case1 = str1[i] + dp[i + 1][j]
                    case2 = str2[j] + dp[i][j + 1]
                    if len(case1) <= len(case2):
                        dp[i][j] = case1
                    else:
                        dp[i][j] = case2
        return dp[0][0]
            