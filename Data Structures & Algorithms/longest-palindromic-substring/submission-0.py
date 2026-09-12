class Solution:

    def longestPalindrome(self, s: str) -> str:
        start = 0          # Starting index of longest palindrome found
        max_len = 1        # Length of longest palindrome found

        def expand(left, right):
            # Expand while characters on both sides are equal
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # left and right are now one step outside the palindrome
            palindrome_start = left + 1
            palindrome_length = right - left - 1

            return palindrome_start, palindrome_length

        for i in range(len(s)):

            # Case 1: Odd-length palindrome
            # Example: "aba"
            # Center is at one character
            curr_start, curr_len = expand(i, i)

            if curr_len > max_len:
                start = curr_start
                max_len = curr_len

            # Case 2: Even-length palindrome
            # Example: "abba"
            # Center is between two characters
            curr_start, curr_len = expand(i, i + 1)

            if curr_len > max_len:
                start = curr_start
                max_len = curr_len

        # Return the longest palindromic substring
        return s[start:start + max_len]