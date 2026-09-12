class Solution:

    def encode(self, s: str) -> str:
        memo = {}

        def solve(st):
            # If already solved, reuse the answer
            if st in memo:
                return memo[st]

            n = len(st)

            # -----------------------------------
            # OPTION 1:
            # Original string ko waise hi rakho
            # -----------------------------------
            best = st


            # -----------------------------------
            # OPTION 2:
            # Har possible split try karo
            #
            # st = left + right
            #
            # answer =
            # solve(left) + solve(right)
            # -----------------------------------
            for i in range(1, n):

                left = st[:i]
                right = st[i:]

                encoded_left = solve(left)
                encoded_right = solve(right)

                candidate = encoded_left + encoded_right

                if len(candidate) < len(best):
                    best = candidate


            # -----------------------------------
            # OPTION 3:
            # Check karo kya poori string
            # kisi pattern ka repetition hai
            #
            # Example:
            # "abababab"
            #
            # pattern = "ab"
            # times = 4
            #
            # candidate = 4[ab]
            # -----------------------------------
            for pattern_len in range(1, n // 2 + 1):

                # Pattern poori string ko exactly divide
                # karna chahiye
                if n % pattern_len != 0:
                    continue

                pattern = st[:pattern_len]
                times = n // pattern_len

                # Check:
                # kya pattern ko 'times' repeat karne par
                # original string milti hai?
                if pattern * times == st:

                    # Pattern khud bhi compress ho sakta hai,
                    # isliye solve(pattern)
                    encoded_pattern = solve(pattern)

                    candidate = (
                        str(times)
                        + "["
                        + encoded_pattern
                        + "]"
                    )

                    if len(candidate) < len(best):
                        best = candidate


            # Save result
            memo[st] = best

            return best

        return solve(s)