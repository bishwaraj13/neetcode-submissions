class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        # dp[i][j] stores LCS length for text1[:i] and text2[:j]
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        def recr(m_index, n_index):
            # Base condition
            if m_index == 0 or n_index == 0:
                return 0

            # Already computed
            if dp[m_index][n_index] != -1:
                return dp[m_index][n_index]

            # Characters match
            if text1[m_index - 1] == text2[n_index - 1]:
                dp[m_index][n_index] = (
                    1 + recr(m_index - 1, n_index - 1)
                )

            # Characters don't match
            else:
                dp[m_index][n_index] = max(
                    recr(m_index, n_index - 1),
                    recr(m_index - 1, n_index)
                )

            return dp[m_index][n_index]

        return recr(m, n)