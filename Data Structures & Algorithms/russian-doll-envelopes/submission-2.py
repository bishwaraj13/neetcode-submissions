class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # Step 1:
        # Sort envelopes by:
        #   1. width ascending
        #   2. height descending when widths are equal
        #
        # Why height descending for same width?
        #
        # Example:
        # [2, 3], [2, 4]
        #
        # These two envelopes CANNOT fit into each other because
        # their widths are equal.
        #
        # If we sorted heights ascending, we would get:
        # [2,3], [2,4]
        #
        # and heights 3 -> 4 would look like a valid increasing
        # subsequence, which would be wrong.
        #
        # Sorting same-width envelopes by height descending prevents
        # them from being selected together in the LIS.
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Binary search helper:
        #
        # Find the first index where arr[index] >= target.
        #
        # This is LOWER BOUND.
        #
        # If no such value exists, return len(arr).
        def lower_bound(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if arr[mid] >= target:
                    # mid could be the answer,
                    # but there may be an earlier valid index.
                    right = mid - 1
                else:
                    # arr[mid] < target,
                    # so answer must be on the right.
                    left = mid + 1

            return left

        # After sorting, width condition is already handled.
        #
        # Now the problem becomes:
        #
        # Find the Longest Increasing Subsequence (LIS)
        # using only the heights.
        #
        # tails[i] =
        # smallest possible ending height of an increasing
        # subsequence of length i + 1.
        #
        # Important:
        # tails is NOT necessarily the actual LIS.
        # But len(tails) is always the LIS length.
        tails = []

        for width, height in envelopes:

            # Find where this height should go.
            #
            # We use lower_bound because we want a STRICTLY
            # increasing subsequence.
            #
            # So we find the first value >= height.
            pos = lower_bound(tails, height)

            if pos == len(tails):
                # height is greater than every value currently
                # in tails.
                #
                # So we can extend the longest subsequence.
                tails.append(height)

            else:
                # Replace the current ending value with a
                # smaller/better ending height.
                #
                # This does NOT increase the LIS length.
                # It only makes this subsequence easier to
                # extend in the future.
                tails[pos] = height

        # Number of entries in tails =
        # maximum number of envelopes we can Russian-doll.
        return len(tails)