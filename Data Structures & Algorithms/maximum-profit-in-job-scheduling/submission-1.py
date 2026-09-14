# This solution is Recursion + Memoization
# But below I use Binary Search which is more optimized
# class Solution:
#     def jobScheduling(
#         self,
#         startTime: List[int],
#         endTime: List[int],
#         profit: List[int]
#     ) -> int:

#         intervals = sorted(zip(startTime, endTime, profit))
#         cache = {}

#         def dfs(i):
#             # No more jobs left
#             if i == len(intervals):
#                 return 0

#             # Return the already computed result
#             if i in cache:
#                 return cache[i]

#             # Option 1: skip the current job
#             dont_include = dfs(i + 1)

#             # Option 2: include the current job
#             include = intervals[i][2]

#             # Find the first job that does not overlap
#             # with the current job
#             j = i + 1

#             while (
#                 j < len(intervals)
#                 and intervals[j][0] < intervals[i][1]
#             ):
#                 j += 1

#             # Add the maximum profit starting from
#             # the next non-overlapping job
#             include += dfs(j)

#             # Store the better of the two choices
#             cache[i] = max(include, dont_include)

#             return cache[i]

#         return dfs(0)

class Solution:
    def jobScheduling(
        self,
        startTime: List[int],
        endTime: List[int],
        profit: List[int]
    ) -> int:

        intervals = sorted(zip(startTime, endTime, profit))
        cache = {}

        def lower_bound(i, target):
            """
            Find the first index j >= i such that:
            intervals[j][0] >= target
            """

            left = i
            right = len(intervals) - 1
            answer = len(intervals)

            while left <= right:
                mid = (left + right) // 2

                if intervals[mid][0] >= target:
                    answer = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return answer

        def dfs(i):
            # No more jobs left
            if i == len(intervals):
                return 0

            # Return already computed result
            if i in cache:
                return cache[i]

            # Option 1: skip the current job
            dont_include = dfs(i + 1)

            # Option 2: include the current job
            current_end = intervals[i][1]
            current_profit = intervals[i][2]

            next_job = lower_bound(i + 1, current_end)

            include = current_profit + dfs(next_job)

            cache[i] = max(include, dont_include)
            return cache[i]

        return dfs(0)